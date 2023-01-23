from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from DisasterEvents.models import *
from AdminBoundary.models import *

# class LocalSerializer( GeoFeatureModelSerializer):
#     class  Meta:
#         model=Municipality
#         geo_field='geom'
#         fields='__all__'

       
class LocalSerializerWithoutGeom(serializers.ModelSerializer):
    class  Meta:
        model=Municipality
        fields=('palika',)
       

    
class DisasterSerializer(serializers.ModelSerializer):
    municipality=LocalSerializerWithoutGeom()
    class Meta:
        model = Disaster
        geo_field='geom'
        fields = "__all__"
