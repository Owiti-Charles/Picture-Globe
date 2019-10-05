from django.shortcuts import render
from .models import Image


def index(request):
    images = Image.objects.all()
    print (images)
    return render(request, 'pictures/index.html', {'images': images[::-1]})
