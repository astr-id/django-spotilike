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
    artiste = serializers.PrimaryKeyRelatedField(queryset=Artiste.objects.all())
    morceaux = MorceauSerializer(many=True, read_only=True, source='morceau_set')

    class Meta:
        model = Album
        fields = ['id', 'titre', 'date_sortie', 'image', 'artiste', 'morceaux']

    def create(self, validated_data):
        album = Album.objects.create(**validated_data)
        return album
    
    def update(self, instance, validated_data):
        # Supprimer les champs imbriqués de la mise à jour
        validated_data.pop('morceaux', None)  # Ne pas permettre la mise à jour des morceaux
        validated_data.pop('artiste', None)  
        
        # Mise à jour des autres champs de l'album
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

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