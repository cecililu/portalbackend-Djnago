from django.contrib.gis.db import models
# Create your models here.
class Municipality(models.Model):
    palika = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    def __str__(self):
        return str(self.palika) 
    
    
class Ward(models.Model):
    province = models.BigIntegerField()
    district = models.CharField(max_length=50)
    palika = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    ward = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    Municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.palika+"  "+" ward: "+"  " +str( self.ward)    

