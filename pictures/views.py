from django.shortcuts import render
from .models import Image


def index(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'pictures/index.html', {'images': images[::-1]})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_images)
        return render(request, 'pictures/search_results.html', {"message": message, "images": searched_images})
