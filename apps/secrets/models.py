from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Secrets(models.Model):
    secret = models.CharField(max_length=255)
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
