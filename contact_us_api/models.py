from django.db import models
import datetime

# Create your models here.

# class queryType(models.Model):
    # qid = 
    
class ContactUs(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=500,null=True, blank=True)
    queryType = models.TextField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)