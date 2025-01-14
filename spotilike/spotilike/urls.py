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
from rest_framework.routers import DefaultRouter

# Importation des vues
from .views import (
    AlbumViewSet, ArtisteViewSet, AlbumSongsView,
    GenreViewSet, ArtistSongsView, MorceauViewSet
)

# Configuration du routeur DRF pour gérer les routes
router = DefaultRouter()

# Enregistrement des ViewSets dans le routeur
router.register(r'api/albums', AlbumViewSet, basename='album')  # Routes pour les albums
router.register(r'api/artists', ArtisteViewSet, basename='artist')  # Routes pour les artistes
router.register(r'api/genres', GenreViewSet, basename='genre')  # Routes pour les genres
router.register(r'api/songs', MorceauViewSet, basename='morceau')  # Routes pour les morceaux

urlpatterns = [
    path('admin/', admin.site.urls), # Route pour l'interface d'administration
    path('', include(router.urls)), # Inclusion des routes générées par le routeur DRF
    # Route personnalisées
    path('api/albums/<int:pk>/songs', AlbumSongsView.as_view(), name='album-songs'),
    path('api/artists/<int:pk>/songs', ArtistSongsView.as_view(), name='artist-songs'),
]