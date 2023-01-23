from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from DisasterEvents.views import *

router = routers.DefaultRouter()
router.register('disaster',DiasterView )

 

urlpatterns = [    
    path('api/',include(router.urls)),
    # path('api/search/custom',DisasterWardWise.as_view()) 
    path('custom',DisasterMunicipalityWise.as_view())
]
