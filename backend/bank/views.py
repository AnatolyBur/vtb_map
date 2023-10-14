from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

class DepartmentFilter(filters.FilterSet):
    ramp = filters.NumberFilter(method='make_ramp')
    def make_ramp(self, queryset, name, value):
        return queryset.filter(special__ramp__exact=int(value))
    
    prime = filters.NumberFilter(method='make_prime')
    def make_prime(self, queryset, name, value):
        return queryset.filter(special__Prime__exact=int(value))
    
    person = filters.NumberFilter(method='make_person')
    def make_person(self, queryset, name, value):
        return queryset.filter(special__person__exact=int(value))
    
    vip_zone = filters.NumberFilter(method='make_vip_Zone')
    def make_vip_Zone(self, queryset, name, value):
        return queryset.filter(special__vipZone__exact=int(value))
    
    juridical = filters.NumberFilter(method='make_juridical')
    def make_juridical(self, queryset, name, value):
        return queryset.filter(special__juridical__exact=int(value))
    
    vip_office = filters.NumberFilter(method='make_vip_office')
    def make_vip_office(self, queryset, name, value):
        return queryset.filter(special__vipOffice__exact=int(value))

    class Meta:
        model = Department
        fields = [
            'ramp',
            'service',
            'prime',
            'person',
            'vip_zone',
            'juridical',
            'vip_office'
        ]

 
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter

    def get_queryset(self):
        req = self.request
        point = req.GET.get('p', '37.573856,55.751574').split(',')
        ref_location = Point(float(point[0]), float(point[1]), srid=4326)

        qs = Department.objects.all().annotate(distance=Distance('coordinates' , ref_location)).order_by('distance')
        return qs


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
