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
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import InscriptionView

# Importation des vues
from .views import (
    AlbumView, AlbumDetailView, AlbumSongsView, ArtisteView,
    UserDetailView, ArtistSongsView, GenreView, ArtisteDetailView, GenreUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/albums/', AlbumView.as_view(), name='album-list-create'),
    path('api/albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('api/albums/<int:pk>/songs/', AlbumSongsView.as_view(), name='album-songs'),
    path('api/genres/', GenreView.as_view(), name='genre-list-create'),
    path('api/genres/<int:pk>/', GenreUpdateView.as_view(), name='genre'),
    path('api/artists/', ArtisteView.as_view(), name='artist-list-create'),
    path('api/artists/<int:pk>/songs/', ArtistSongsView.as_view(), name='artist-songs'),
    path('api/artists/<int:pk>/', ArtisteDetailView.as_view(), name='artist-detail'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/users/signup/', InscriptionView.as_view(), name='signup'),
    path('api/users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
