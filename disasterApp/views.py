from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework  import filters as rest_filters
from disasterApp.models import *
from disasterApp.serializer import *

from django_filters import rest_framework as filters

class DiasterView(viewsets.ModelViewSet):
        queryset = Disaster.objects.all()
        serializer_class = DisasterSerializer

class LocalsView(viewsets.ModelViewSet):
        queryset =Local.objects.all()
        serializer_class = LocalSerializer

#   filterclass
# class NameFilter(filters.FilterSet):
#     name = filters.CharFilter(field_name='name',lookup_expr='^name')
#     class Meta:
#         model = Disaster
#         fields = ['name']    
              
class DisasterWardWise(generics.ListAPIView):
        queryset=Disaster.objects.all()
        serializer_class=DisasterSerializer
        filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter]
        filterset_fields = ['municipality','name']
        search_fields = ['name']
        # filterset_class = NameFilter
        