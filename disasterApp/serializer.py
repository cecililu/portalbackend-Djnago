from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from disasterApp.models import *

# class LocalSerializer( GeoFeatureModelSerializer):
#     class  Meta:
#         model=Local
#         geo_field='geom'
#         fields='__all__'
       
# class LocalSerializerWithoutGeom(serializers.ModelSerializer):
#     class  Meta:
#         model=Local
#         fields=['pr_name', 'local', 'type']
    
class DisasterSerializer( GeoFeatureModelSerializer):
    municipality=LocalSerializerWithoutGeom()
    class Meta:
        model = DisasterEvent
        geo_field='geom'
        fields = "__all__"
