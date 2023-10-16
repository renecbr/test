from django.urls import path

from measurement.views import SensorCreateView, MeasurementCreateView, SingleView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SingleView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
