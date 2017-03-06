from django.contrib import admin

#importing the models
from .models import *
# Register your models here.
admin.site.register(Upload)


class UploadAdmin(admin.ModelAdmin):
	class meta:
		model = Upload
		fields = ['description',]