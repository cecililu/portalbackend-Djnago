from django.shortcuts import render
from rest_framework import viewsets
from disasterApp.models import *

class DiasterView(viewsets.ViewSet):
 
        queryset = Disaster.objects.all()
        serializer_class = DisasterSerializer
   