from django.db import models

# Create your models here.
class geolocation(models.Model):
   Id= models.IntegerField()
   Name= models.CharField(max_length=200, default="a")
   Latitude= models.DecimalField(max_digits=12, decimal_places=8, default=0)
   Longitude= models.DecimalField(max_digits=12, decimal_places=8, default=0)

class custom_user(models.Model):
   Id= models.IntegerField()
   first_name= models.TextField()
   last_name= models.TextField()
   email= models.TextField()
   password= models.TextField()
   phone= models.TextField()
