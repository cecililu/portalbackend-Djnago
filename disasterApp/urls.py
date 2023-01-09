from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from disasterApp.views import *


router = routers.DefaultRouter()
router.register('disaster',DiasterView )
router.register('locals',LocalsView)

urlpatterns = [    
    path('/api/',include(routers.urls)),
]
