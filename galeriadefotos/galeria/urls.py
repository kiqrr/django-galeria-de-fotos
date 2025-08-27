from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
]
