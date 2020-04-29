# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#ccc_patients_status 
testing_status = (
    ('Select', 'SELECT'),
    ('positive', 'POSITIVE'),
    ('negative', 'NEGATIVE'),
)

class ccc(models.Model): #Model for Covid Care Centres
    ccc_hospitalname = models.CharField(max_length=100)
    ccc_patientsname = models.CharField(max_length=140)
    ccc_patients_status = models.CharField(max_length=10, choices = testing_status, default='select')
    ccc_no_of_beds = models.CharField(max_length=5)

    def get_absolute_url(self): 
        return reverse('index')

 