from django.db import models
from django.contrib.auth.models import AbstractUser
from AdminBoundary.models import *
# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    isCDO = models.BooleanField(default=False,null=True,blank=True)
    is_cluster = models.BooleanField(default=False,null=True,blank=True)
    ward=models.ForeignKey(Ward,on_delete=models.CASCADE,null=True,blank=True)
    Municipality=models.ForeignKey(Municipality,on_delete=models.CASCADE,null=True,blank=True)
    