from rest_framework import serializers
from .models import Album, Artiste, Genre, Morceau, Utilisateur

class MorceauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morceau
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artiste = ArtisteSerializer() 
    morceaux = MorceauSerializer(many=True, read_only=True, source='morceau_set') 

    class Meta:
        model = Album
        fields = ['id', 'titre', 'date_sortie', 'image', 'artiste', 'morceaux']


class UtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = Utilisateur.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user