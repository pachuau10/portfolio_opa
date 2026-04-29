from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]