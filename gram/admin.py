from django.contrib import admin
from .models import Image, Profile
from django.contrib.sites.models import Site

# Register your models here.
# Register image and profile model
admin.site.register(Image)
admin.site.register(Profile)
