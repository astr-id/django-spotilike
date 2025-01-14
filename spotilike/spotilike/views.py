from rest_framework.viewsets import ModelViewSet
from .models import Album, Artiste, Genre
from .serializers import AlbumSerializer, ArtisteSerializer, GenreSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Morceau
from .serializers import MorceauSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
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

class AlbumSongsView(APIView):
    def get(self, request, pk):
        morceaux = Morceau.objects.filter(album_id=pk)
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)

class ArtistSongsView(APIView):
    def get(self, request, pk):
        morceaux = Morceau.objects.filter(album__artiste_id=pk)
        serializer = MorceauSerializer(morceaux, many=True)
        return Response(serializer.data)
