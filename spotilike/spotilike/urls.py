"""
URL configuration for spotilike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import (
    AlbumViewSet, ArtisteViewSet, AlbumSongsView,
    GenreViewSet, ArtistSongsView, MorceauViewSet
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'api/albums', AlbumViewSet, basename='album')
router.register(r'api/artists', ArtisteViewSet, basename='artist')
router.register(r'api/genres', GenreViewSet, basename='genre')
router.register(r'api/songs', MorceauViewSet, basename='morceau')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
    path('api/albums/<int:pk>/songs', AlbumSongsView.as_view(), name='album-songs'),
    path('api/artists/<int:pk>/songs', ArtistSongsView.as_view(), name='artist-songs'),
]
