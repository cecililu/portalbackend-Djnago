from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework  import filters as rest_filters
from disasterApp.models import *
from disasterApp.serializer import *

from django_filters import rest_framework as filters

class DiasterView(viewsets.ModelViewSet):
        queryset = DisasterEvent.objects.all()
        serializer_class = DisasterSerializer

class LocalsView(viewsets.ModelViewSet):
        queryset =Local.objects.all()
        serializer_class = LocalSerializer


              
class DisasterWardWise(generics.ListAPIView):
        queryset=DisasterEvent.objects.all()
        serializer_class=DisasterSerializer
        filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
        filterset_fields = ['municipality__local','name']
        search_fields = ['name','municipality__local']
        ordering_fields=['name','municipality__local']
        
