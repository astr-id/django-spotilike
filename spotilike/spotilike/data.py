import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotilike.settings') 
django.setup()

from datetime import datetime
from spotilike.models import Artiste, Genre, Morceau, GenreHasMorceau, Album

def populate_database():
    # Création des artistes
    artiste1 = Artiste.objects.create(
        nom="Taylor Swift",
        avatar="https://example.com/taylor_swift_avatar.jpg",
        biographie="Taylor Swift est une auteure-compositrice-interprète américaine, célèbre pour ses chansons mélodiques et ses paroles évocatrices."
    )
    artiste2 = Artiste.objects.create(
        nom="Drake",
        avatar="https://example.com/drake_avatar.jpg",
        biographie="Drake est un rappeur, chanteur et producteur canadien, connu pour sa polyvalence musicale et ses collaborations internationales."
    )

    artiste3 = Artiste.objects.create(
        nom="Billie Eilish", 
        avatar="https://example.com/billie_eilish_avatar.jpg", 
        biographie="Billie Eilish est une artiste américaine au style unique, mêlant pop alternative et influences sombres."
    )

    artiste4 = Artiste.objects.create(
        nom="Ed Sheeran", 
        avatar="https://example.com/ed_sheeran_avatar.jpg", 
        biographie="Ed Sheeran est un chanteur et compositeur britannique, célèbre pour ses ballades romantiques et ses performances acoustiques."
    )

    artiste5 = Artiste.objects.create(
        nom="BTS", 
        avatar="https://example.com/bts_avatar.jpg", 
        biographie="BTS est un groupe de K-pop sud-coréen qui a conquis le monde avec ses chansons percutantes et ses chorégraphies impressionnantes."
    )

    artiste6 = Artiste.objects.create(
        nom="Adele", 
        avatar="https://example.com/adele_avatar.jpg", 
        biographie="Adele est une chanteuse britannique reconnue pour sa voix puissante et ses ballades émouvantes."
    )

    artiste7 = Artiste.objects.create(
        nom="Post Malone", 
        avatar="https://example.com/post_malone_avatar.jpg", 
        biographie="Post Malone est un rappeur et chanteur américain, connu pour ses chansons mêlant rap, pop et rock."
    )

    artiste8 = Artiste.objects.create(
        nom="The Weeknd", 
        avatar="https://example.com/the_weeknd_avatar.jpg", 
        biographie="The Weeknd est un artiste canadien qui mélange R&B, pop et sonorités électroniques dans ses hits internationaux."
    )

    artiste9 = Artiste.objects.create(
        nom="Dua Lipa", 
        avatar="https://example.com/dua_lipa_avatar.jpg", 
        biographie="Dua Lipa est une chanteuse britannique, connue pour ses tubes pop dansants et son style distinctif."
    )

    artiste10 = Artiste.objects.create(
        nom="Bad Bunny", 
        avatar="https://example.com/bad_bunny_avatar.jpg", 
        biographie="Bad Bunny est un chanteur portoricain, pionnier de la musique reggaeton et trap latino."
    )

# Création des genres
genre1 = Genre.objects.create(titre="Pop", description="Un genre musical populaire, accessible et entraînant.")
genre2 = Genre.objects.create(titre="Hip-Hop", description="Un genre rythmique, souvent lié à la culture urbaine.")
genre3 = Genre.objects.create(titre="R&B", description="Un style mélodique, souvent axé sur les émotions.")
genre4 = Genre.objects.create(titre="K-Pop", description="Un style musical sud-coréen combinant pop, rap et danse.")
genre5 = Genre.objects.create(titre="Rock", description="Un genre énergique, influencé par les guitares électriques.")
genre6 = Genre.objects.create(titre="Electro", description="Un genre basé sur des sons électroniques et des rythmes dansants.")

# Création des albums
album1 = Album.objects.create(titre="Midnights", image="https://example.com/midnights.jpg", date_sortie=datetime(2022, 10, 21), artiste=artiste1)
album2 = Album.objects.create(titre="Certified Lover Boy", image="https://example.com/certified_lover_boy.jpg", date_sortie=datetime(2021, 9, 3), artiste=artiste2)
album3 = Album.objects.create(titre="Happier Than Ever", image="https://example.com/happier_than_ever.jpg", date_sortie=datetime(2021, 7, 30), artiste=artiste3)
album4 = Album.objects.create(titre="=", image="https://example.com/equals.jpg", date_sortie=datetime(2021, 10, 29), artiste=artiste4)
album5 = Album.objects.create(titre="BE", image="https://example.com/be.jpg", date_sortie=datetime(2020, 11, 20), artiste=artiste5)
album6 = Album.objects.create(titre="30", image="https://example.com/30.jpg", date_sortie=datetime(2021, 11, 19), artiste=artiste6)

# Création des morceaux
morceau1 = Morceau.objects.create(titre="Anti-Hero", duree="00:03:21", morceau="anti_hero.mp3", album=album1)
morceau2 = Morceau.objects.create(titre="Way 2 Sexy", duree="00:04:18", morceau="way_2_sexy.mp3", album=album2)
morceau3 = Morceau.objects.create(titre="Happier Than Ever", duree="00:05:35", morceau="happier_than_ever.mp3", album=album3)
morceau4 = Morceau.objects.create(titre="Shivers", duree="00:03:27", morceau="shivers.mp3", album=album4)
morceau5 = Morceau.objects.create(titre="Life Goes On", duree="00:03:27", morceau="life_goes_on.mp3", album=album5)
morceau6 = Morceau.objects.create(titre="Easy On Me", duree="00:03:44", morceau="easy_on_me.mp3", album=album6)

# Association des morceaux aux genres
GenreHasMorceau.objects.create(genre=genre1, morceau=morceau1)  
GenreHasMorceau.objects.create(genre=genre2, morceau=morceau2)  
GenreHasMorceau.objects.create(genre=genre3, morceau=morceau3)  
GenreHasMorceau.objects.create(genre=genre1, morceau=morceau4) 
GenreHasMorceau.objects.create(genre=genre4, morceau=morceau5) 
GenreHasMorceau.objects.create(genre=genre1, morceau=morceau6) 