from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Photo

def index(request):
    photos = Photo.objects.all()
    
    # Handle search query
    search_query = request.GET.get('q')
    if search_query:
        photos = photos.filter(
            Q(title__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    context = {
        'photos': photos,
        'search_query': search_query,
    }
    return render(request, 'galeria/index.html', context)

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'galeria/photo_detail.html', {'photo': photo})
