from django.contrib.gis.db import models
# models.Manager
class Local(models.Model):
    province = models.BigIntegerField()
    pr_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    type = models.CharField(
        max_length=50) 
    geom = models.MultiPolygonField(srid=4326)
    def __str__(self):
        return self.local 

class Ward(models.Model):
    province = models.BigIntegerField()
    district = models.CharField(max_length=50)
    palika = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    ward = models.BigIntegerField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    geom = models.MultiPolygonField(srid=4326)

# Auto-generated `LayerMapping` dictionary for Ward model
# ward_mapping = {
#     'province': 'PROVINCE',
#     'district': 'DISTRICT',
#     'palika': 'PALIKA',
#     'type': 'TYPE',
#     'ward': 'WARD',
#     'geom': 'MULTIPOLYGON',
# }
from django.utils import timezone

class Disaster(models.Model):
    # Local.objects.create
    name=models.CharField(max_length=100)
    municipality=models.ForeignKey(Local,on_delete=models.CASCADE,blank=True,null=True)
    geom=models.GeometryField(blank=True,null=True)
    
    
    date_event= models.DateTimeField(blank=True,default=timezone.now,null=True)
    date_closed=models.DateTimeField(blank=True,null=True)
    is_closed=models.BooleanField(null=True,default=False)
    
    
    date_occurance= models.DateTimeField(blank=True,default=timezone.now,null=True)
    date_closed_d=models.DateTimeField(blank=True,null=True)

class DisasterEvent(models.Model):
    name=models.CharField(max_length=100)
    municipality=models.ForeignKey(Local,on_delete=models.CASCADE,blank=True,null=True)
    geom=models.GeometryField(blank=True,null=True)
    
    date_event= models.DateTimeField(blank=True,default=timezone.now,null=True)
    date_closed=models.DateTimeField(blank=True,null=True)
    is_closed=models.BooleanField(null=True,default=False)
    
    def __str__(self):
        return str(super().__str__())+str(self.name)
    
class Run(models.Model):
    name=models.CharField(max_length=100)