from django import forms
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 
class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True,help_text='Required')
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']


class MoM(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    action_items = models.CharField(max_length=300)
    focus_points = models.CharField(max_length=500)

class feedback(models.Model):
    who_took_the_session = models.CharField(max_length=100)
    rate = models.PositiveSmallIntegerField()
    what_did_you_like = models.CharField(max_length=500)
    what_are_you_expecting = models.CharField(max_length=500)
    date = models.DateField()
    
