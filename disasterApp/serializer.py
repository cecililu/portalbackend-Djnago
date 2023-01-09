from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from disasterApp.models import *

class LocalSerializer( GeoFeatureModelSerializer):
    class  Meta:
        model=Local
        fields='__all__'
     
class DisasterSerializer( GeoFeatureModelSerializer):
    municipality=LocalSerializer
    class Meta:
        model = Disaster
        fields = "__all__"
