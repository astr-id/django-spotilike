from datetime import datetime

from spotilike.spotilike.models import Artiste, Genre, Morceau, GenreHasMorceau, Album

# Création des artistes
artiste1 = Artiste.objects.create(nom="Artiste 1", avatar="url_de_l_avatar1.jpg", biographie="Biographie de l'artiste 1.")
artiste2 = Artiste.objects.create(nom="Artiste 2", avatar="url_de_l_avatar2.jpg", biographie="Biographie de l'artiste 2.")

# Création des genres
genre1 = Genre.objects.create(titre="Rock", description="Un genre musical énergique et puissant.")
genre2 = Genre.objects.create(titre="Pop", description="Un genre musical populaire et accessible.")
genre3 = Genre.objects.create(titre="Jazz", description="Un genre musical improvisé et complexe.")

# Création des albums
album1 = Album.objects.create(titre="Album 1", image="image_album1.jpg", date_sortie=datetime(2022, 5, 10, 14, 30), artiste=artiste1)
album2 = Album.objects.create(titre="Album 2", image="image_album2.jpg", date_sortie=datetime(2023, 8, 25, 20, 00), artiste=artiste2)

# Création des morceaux
morceau1 = Morceau.objects.create(titre="Morceau 1", duree="00:03:45", morceau="fichier_morceau1.mp3", album=album1)
morceau2 = Morceau.objects.create(titre="Morceau 2", duree="00:04:30", morceau="fichier_morceau2.mp3", album=album1)
morceau3 = Morceau.objects.create(titre="Morceau 3", duree="00:03:20", morceau="fichier_morceau3.mp3", album=album2)
morceau4 = Morceau.objects.create(titre="Morceau 4", duree="00:02:55", morceau="fichier_morceau4.mp3", album=album2)

# Association des morceaux aux genres
GenreHasMorceau.objects.create(genre=genre1, morceau=morceau1)
GenreHasMorceau.objects.create(genre=genre2, morceau=morceau2)
GenreHasMorceau.objects.create(genre=genre3, morceau=morceau3)
GenreHasMorceau.objects.create(genre=genre2, morceau=morceau4)