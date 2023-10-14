from .models import *
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    def get_distance(self, obj):
        return obj.distance.m

    s_coordinates = serializers.SerializerMethodField()

    def get_s_coordinates(self, obj):
        return obj.coordinates.coords

    class Meta:
        model = Department
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
