from django.db import models
from django.contrib.gis.db import models


class Local(models.Model):
    province = models.BigIntegerField()
    pr_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for Local model
# local_mapping = {
#     'province': 'PROVINCE',
#     'pr_name': 'PR_NAME',
#     'district': 'DISTRICT',
#     'local': 'LOCAL',
#     'type': 'TYPE',
#     'geom': 'MULTIPOLYGON',
# }

class Disaster(models.Model):
    name=models.CharField(max_length=100)
    