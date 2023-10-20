from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user_status = User.objects.filter(username=request.user).values('is_staff')
        if request.method == 'GET' or user_status[0]['is_staff'] is True:
            return True
        return request.user == obj.creator