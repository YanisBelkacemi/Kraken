#NEEDS A FUCKING REVIEW 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from User.models import Users
from django.utils import timezone
class ApiKeys(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    key_prefix = models.CharField(max_length=10)
    key_hash = models.TextField()
    name = models.CharField(max_length=50, blank=True, null=True)
    revoked = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    last_used = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'api_keys'
        