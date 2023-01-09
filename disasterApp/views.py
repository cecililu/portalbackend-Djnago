from django.shortcuts import render
from rest_framework import viewsets
from disasterApp.models import *
from disasterApp.serializer import *


class DiasterView(viewsets.ModelViewSet):
        queryset = Disaster.objects.all()
        serializer_class = DisasterSerializer

class LocalsView(viewsets.ModelViewSet):
        queryset =Local.objects.all()
        serializer_class = LocalSerializer
   