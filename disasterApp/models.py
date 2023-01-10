
from django.contrib.gis.db import models

class Local(models.Model):
    
    province = models.BigIntegerField()
    pr_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    type = models.CharField(max_length=50) 
    
    geom = models.MultiPolygonField(srid=4326)
      
    
    def __str__(self):
        return self.local

# Auto-generated `LayerMapping` dictionary for Local model
# local_mapping = {
#     'province': 'PROVINCE',
#     'pr_name': 'PR_NAME',
#     'district': 'DISTRICT',
#     'local': 'LOCAL',
#     'type': 'TYPE',
#     'geom': 'MULTIPOLYGON',
# }
from django.utils import timezone

class Disaster(models.Model):
    name=models.CharField(max_length=100)
    municipality=models.ForeignKey(Local,on_delete=models.CASCADE,blank=True,null=True)
    
    geom=models.GeometryField(blank=True,null=True)
    
    # date_event= models.DateTimeField(blank=True,default=timezone.now(),null=True)
    # date_closed=models.DateTimeField(blank=True,null=True)

    
    # is_closed=models.DateField(null=True,default=False)
    date_occurance= models.DateTimeField(blank=True,default=timezone.now,null=True)
    date_closed_d=models.DateTimeField(blank=True,null=True)