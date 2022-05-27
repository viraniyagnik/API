from django.contrib import admin

# Register your models here.
from .models import geolocation
from .models import custom_user

admin.site.register(geolocation)
admin.site.register(custom_user)