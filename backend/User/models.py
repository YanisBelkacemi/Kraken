from django.db import models
from django.contrib.auth.models import PermissionsMixin , AbstractBaseUser
from .CustomUserManager import CustomUserManager
# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=False, max_length=255)
    password = models.TextField()
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    UserInputID = models.CharField(db_column='UserInputID', unique=True, max_length=10)  # Field name made lowercase.
    UserOutputID = models.CharField(db_column='UserOutputID', unique=True, max_length=10)  # Field name made lowercase.
    
    #this here is used for login
    objects = CustomUserManager()
    class Meta:
        managed = True
        db_table = 'users'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 