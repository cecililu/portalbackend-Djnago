from django.shortcuts import render
from rest_framework import viewsets
from disasterApp.models import *
from disasterApp.serializer import *


class DiasterView(viewsets.ViewSet):
        queryset = Disaster.objects.all()
        serializer_class = DisasterSerializer

class LocalsView(viewsets.ViewSet):
        queryset =Local.objects.all()
        serializer_class = LocalSerializer
   