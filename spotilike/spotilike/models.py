from django.db import models
from django.contrib.auth.models import AbstractUser

# personnalisation du user de django
class Utilisateur(AbstractUser):
    # Nom d’utilisateur (username) et Mot de passe (password) sont déjà gérés par Django via AbstractUser, donc tu n’as pas besoin de les redéfinir. :Ces champs sont déjà inclus par défaut, tu n'as pas besoin de les redéfinir ici
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    biographie = models.TextField(null=True, blank=True)  
    email = models.EmailField(unique=True)  # Le champ email est déjà présent par défaut avec une contrainte d'unicité

    def __str__(self):
        return self.username


class Artiste(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    biographie = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titre


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=45)
    date_sortie = models.DateField()
    image = models.CharField(max_length=255, null=True, blank=True)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Morceau(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=45)
    duree = models.TimeField()
    morceau = models.CharField(max_length=45)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class GenreHasMorceau(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    morceau = models.ForeignKey(Morceau, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('genre', 'morceau')

    def __str__(self):
        return f'{self.genre} - {self.morceau}'
