from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Disaster)
admin.site.register(DisasterType)
admin.site.register(Rating)