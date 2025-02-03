from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.shortcuts import get_object_or_404

from .models import Album, Artiste, Genre, Morceau, Utilisateur
from .serializers import AlbumSerializer, ArtisteSerializer, GenreSerializer, MorceauSerializer, UtilisateurSerializer

class AlbumView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        albums = Album.objects.all()  # Récupérer tous les albums de la base de données.
        serializer = AlbumSerializer(albums, many=True)  
        return Response(serializer.data)  
    
    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(): # Vérifier si les données sont valides.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
    
    def put(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenreView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

class GenreUpdateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtisteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data)

class ArtisteDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def put(self, request, pk):
        artiste = get_object_or_404(Artiste, pk=pk)
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        artiste = get_object_or_404(Artiste, pk=pk)
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlbumSongsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        morceaux = Morceau.objects.filter(album_id=pk)
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        data = request.data.copy()
        data["album"] = pk
        serializer = MorceauSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistSongsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        morceaux = Morceau.objects.filter(album__artiste_id=pk)
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)

class UserDetailView(APIView):
    
    def delete(self, request, pk):
        user = get_object_or_404(Utilisateur, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InscriptionView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)