from django.contrib.gis.db import models
from AdminBoundary.models import *
# Create your models here.
class DisasterType(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    order = models.IntegerField()

class Rating(models.Model):
    order = models.IntegerField()

class Disaster(models.Model):
    name = models.CharField(max_length=255)
    geom = models.GeometryField(srid=4326)
    registered_date_time = models.DateTimeField()
    update_date_time = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    type = models.ForeignKey(DisasterType, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    
    
    