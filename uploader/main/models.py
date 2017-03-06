from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Upload(models.Model):
	description = models.CharField(max_length=255, blank=True)
	uploaded_at = models.FileField(upload_to='documents/')
	timestamp = models.DateTimeField(auto_now_add=True)


