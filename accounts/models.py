from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_CDO=models.BooleanField(default=False)
    is_Municipality=models.BooleanField(default=False)  
    is_Ward=models.BooleanField(default=False) 
    is_cluster=models.BooleanField(default=False) 
      
    
    