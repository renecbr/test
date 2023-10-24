import pytest

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'id': 1})
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_course_id_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'id': courses[0].id})
    assert response.status_code == 200
    data = response.json()
    for d in data:
        assert d['id'] == courses[0].id
    assert len(data) > 0


@pytest.mark.django_db
def test_course_name_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'name': courses[0].name})
    assert response.status_code == 200
    data = response.json()
    for d in data:
        assert d['name'] == courses[0].name
    assert len(data) > 0


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'course1'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    id = courses[0].id
    response = client.patch('/api/v1/courses/' + str(id) + '/', data={'name': 'course2'})
    assert response.status_code == 200
    data = response.json()
    if data['id'] == 1:
        assert data['name'] == 'course2'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    id = courses[0].id
    response = client.delete('/api/v1/courses/' + str(id) + '/')
    assert response.status_code == 204

