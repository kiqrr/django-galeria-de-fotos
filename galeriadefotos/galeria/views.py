from django.shortcuts import render, get_object_or_404
from .models import Photo

def index(request):
    photos = Photo.objects.all()
    return render(request, 'galeria/index.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'galeria/photo_detail.html', {'photo': photo})
