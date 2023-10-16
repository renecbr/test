# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from requests import Response
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def sensor_create(self, serializer):
        name = get_object_or_404(Sensor, name=self.request.data.get('name'))
        description = get_object_or_404(Sensor, description=self.request.data.get('description'))
        return serializer.save(name=name, description=description)


class SingleView(RetrieveUpdateAPIView,):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def measurement_create(self, serializer):
        sensor = get_object_or_404(Measurement, sensor=self.request.data.get('sensor'))
        temperature = get_object_or_404(Measurement, temperature=self.request.data.get('temperature'))
        return serializer.save(sensor=sensor, temperature=temperature)


