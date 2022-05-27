from django.shortcuts import render
from .models import geolocation

# Create your views here.
def index(request):
    obj = geolocation.objects.all()
    context = {
        "obj":obj,
    }
    return render(request,"index.html", context)
