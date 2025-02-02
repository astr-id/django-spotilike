from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Album, Artiste, Genre, Morceau, Utilisateur
from .serializers import AlbumSerializer, ArtisteSerializer, GenreSerializer, MorceauSerializer, UtilisateurSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ViewSets pour gérer les opérations CRUD

class AlbumViewSet(ModelViewSet):
    # Récupère tous les albums de la base de données
    queryset = Album.objects.all()
    # Spécifie le sérialiseur pour le modèle Album
    serializer_class = AlbumSerializer
    # Spécifie les permissions pour cette vue
    permission_classes = [IsAuthenticatedOrReadOnly]

class ArtisteViewSet(ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MorceauViewSet(ModelViewSet):
    queryset = Morceau.objects.all()
    serializer_class = MorceauSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Vue API personnalisée

class AlbumSongsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        # Récupère tous les morceaux de l'album spécifié
        morceaux = Morceau.objects.filter(album_id=pk)
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            album = Album.objects.get(pk=pk)  # Vérifie si l'album existe
        except Album.DoesNotExist:
            return Response({"error": "Album not found"}, status=status.HTTP_404_NOT_FOUND)

        # Ajoute l'ID de l'album dans les données avant la validation
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
        # Filtre les morceaux associés à l'artiste via les albums
        morceaux = Morceau.objects.filter(album__artiste_id=pk)
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)
    
class InscriptionView(APIView):
    def post(self, request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]