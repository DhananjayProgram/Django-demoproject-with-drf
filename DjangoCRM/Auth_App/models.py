from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

TEAM_CHOICES = ( 
    ("software", "Software Team"), 
    ("hardware", "Hardware Team"), 
    ("operation", "Operation Team"), 
    
)


class CustomUser(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length = 20, choices = TEAM_CHOICES, default = 'software') 
    user_profile_image = models.ImageField(upload_to="profile")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.first_name +" "+ self.last_name
    

    

