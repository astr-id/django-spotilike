from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Album, Artiste, Genre, Morceau
from .serializers import AlbumSerializer, ArtisteSerializer, GenreSerializer, MorceauSerializer, UtilisateurSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# ViewSets pour gérer les opérations CRUD

class AlbumViewSet(ModelViewSet):
    # Récupère tous les albums de la base de données
    queryset = Album.objects.all()
    # Spécifie le sérialiseur pour le modèle Album
    serializer_class = AlbumSerializer

class ArtisteViewSet(ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MorceauViewSet(ModelViewSet):
    queryset = Morceau.objects.all()
    serializer_class = MorceauSerializer


# Vue API personnalisée

class AlbumSongsView(APIView):
    def get(self, request, pk):
        # Filtre les morceaux associés à l'album dont l'id est `pk`
        morceaux = Morceau.objects.filter(album_id=pk)
        # Sérialise les morceaux pour les retourner sous forme de JSON
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)

class ArtistSongsView(APIView):
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