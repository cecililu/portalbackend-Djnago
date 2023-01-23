
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework  import filters as rest_filters
from DisasterEvents.models import Disaster
from .serializer import *

from django_filters import rest_framework as filters

class DiasterView(viewsets.ModelViewSet):
        queryset = Disaster.objects.all()
        serializer_class = DisasterSerializer

# class LocalsView(viewsets.ModelViewSet):
#         queryset =Local.objects.all()
#         serializer_class = LocalSerializer


       
# class DisasterWardWise(generics.ListAPIView):
#         queryset=DisasterEvent.objects.all()
#         serializer_class=DisasterSerializer
#         filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
#         filterset_fields = ['municipality__local','name']
#         search_fields = ['name','municipality__local']
#         ordering_fields=['name','municipality__local']
        
class DisasterMunicipalityWise(generics.ListAPIView):
        queryset=Disaster.objects.all()
        serializer_class=DisasterSerializer
        
        # filter_backends=[filters.DjangoFilterBackend,]
        # filterset_fields = ['municipality__municipality','palika']
        # search_fields = ['name','municipality__local']
        # ordering_fields=['name','municipality__local']
        
        filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
        filterset_fields = ['municipality__palika']
        search_fields = ['name','municipality__local']
        ordering_fields=['name','municipality__local']