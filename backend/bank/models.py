from django.db import models
from django.contrib.gis.db import models as models_gis

class Service(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    def __str__(self):
        return f'{self.title}'

class City(models.Model):
    title = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    def __str__(self):
        return f'{self.title}'


class Department(models.Model):
    short_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    scheduleFl = models.CharField(max_length=255)
    scheduleJurL = models.CharField(max_length=255)
    coordinates = models_gis.PointField(null=False, blank=False, srid=4326)
    service = models.ManyToManyField(Service, blank=True)
    special = models.JSONField(null=True, blank=True)
    biskvit_id = models.CharField(max_length=255, default='')
    current_workload = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return f'{self.short_name}'


class WorkloadTime(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    value = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Нагрузка'
        verbose_name_plural = 'Нагрузки'

    def __str__(self):
        return f'{self.department}-{self.date}: {self.value}'