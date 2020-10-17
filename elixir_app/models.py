from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django import forms

# Create your models here.
import os

from django.utils import timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))


class Insert(models.Model):
    filepaths = models.FileField(max_length=200,upload_to=os.path.join(BASE_DIR,'images'))
    filename = models.CharField(max_length=100)
    upload_date = models.DateTimeField(default=timezone.now)



class  PatientDetails(models.Model):
    cardid = models.CharField(max_length=255,unique=True,primary_key=True)
    BLOOD_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        
    )
    blood = models.CharField(max_length=100,choices=BLOOD_CHOICES)
    
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    # def get_cardid(self):
    #     """used to get patient's card ID number"""

    #     return self.cardid
    
    # def get_blood(self):
    #     """ used to get patient blood group type"""

    #     return self.blood

    # def get_age(self):
    #     """gets patient age"""
    #     return self.age
    

    # def get_address(self):
    #     """gets patient address"""
    #     return self.address






    