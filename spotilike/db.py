import os
import django
from django.utils import timezone
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotilike.settings')
django.setup()

from spotilike.models import Artiste, Genre, Album, Morceau, GenreHasMorceau

# Datas artistes
def create_artistes():
    artistes_data = [
        Artiste(nom="Taylor Swift", avatar="https://i.scdn.co/image/ab6761610000e5ebe672b5f553298dcdccb0e676", 
                biographie="Taylor Swift est une auteure-compositrice-interprète américaine."),
        Artiste(nom="Drake", avatar="https://i.scdn.co/image/ab6761610000e5eb4293385d324db8558179afd9", 
                biographie="Drake est un rappeur et producteur canadien, connu pour sa polyvalence musicale."),
        Artiste(nom="Billie Eilish", avatar="https://i.scdn.co/image/ab6761610000e5eb4a21b4760d2ecb7b0dcdc8da", 
                biographie="Billie Eilish est une artiste américaine au style unique, mêlant pop alternative et influences sombres."),
        Artiste(nom="Ed Sheeran", avatar="https://i.scdn.co/image/ab6761610000e5eb784daff754ecfe0464ddbeb9", biographie="Ed Sheeran est un chanteur et compositeur britannique, célèbre pour ses ballades romantiques et ses performances acoustiques."),
        Artiste(nom="BTS", avatar="https://i.scdn.co/image/ab6761610000e5ebd642648235ebf3460d2d1f6a", biographie="BTS est un groupe de K-pop sud-coréen qui a conquis le monde avec ses chansons percutantes et ses chorégraphies impressionnantes."),
        Artiste(nom="Adele", avatar="https://i.scdn.co/image/ab6761610000e5eb68f6e5892075d7f22615bd17", biographie="Adele est une chanteuse britannique reconnue pour sa voix puissante et ses ballades émouvantes."),
        Artiste(nom="Post Malone", avatar="https://m.media-amazon.com/images/M/MV5BN2VmNDI3OWUtMGEyYS00Njg5LTlkNDUtOTI1MDk5MjdmYmExXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg", biographie="Post Malone est un rappeur et chanteur américain, connu pour ses chansons mêlant rap, pop et rock."),
        Artiste(nom="The Weeknd", avatar="https://i.scdn.co/image/ab6761610000e5eb9e528993a2820267b97f6aae", biographie="The Weeknd est un artiste canadien qui mélange R&B, pop et sonorités électroniques dans ses hits internationaux."),
        Artiste(nom="Dua Lipa", avatar="https://i.scdn.co/image/ab67616d00001e022172b607853fa89cefa2beb4", biographie="Dua Lipa est une chanteuse britannique, connue pour ses tubes pop dansants et son style distinctif."),
        Artiste(nom="Bad Bunny", avatar="https://i.scdn.co/image/ab67616100005174744a4243fb6cc938011a98f4", biographie="Bad Bunny est un chanteur portoricain, pionnier de la musique reggaeton et trap latino.")
    ]
    Artiste.objects.bulk_create(artistes_data)


# Datas genres
def create_genres():
    genres_data = [
        Genre(titre="Pop", description="Un genre musical populaire et entraînant."),
        Genre(titre="Hip-Hop", description="Un genre rythmique, souvent associé à la culture urbaine."),
        Genre(titre="R&B", description="Un style mélodique, souvent axé sur les émotions."),
        Genre(titre="K-Pop", description="Un genre musical sud-coréen combinant pop, rap et danse."),
        Genre(titre="Rock", description="Un genre énergique, influencé par les guitares électriques."),
        Genre(titre="Electro", description="Un genre basé sur des sons électroniques et des rythmes dansants.")
        ]
    Genre.objects.bulk_create(genres_data)


# Datas albums
def create_albums():
    albums_data = [
        Album(titre="Midnights", image="https://i.scdn.co/image/ab67616d0000b273bb54dde68cd23e2a268ae0f5", 
              date_sortie=timezone.make_aware(datetime(2022, 10, 21)), artiste=Artiste.objects.get(nom="Taylor Swift")),
        Album(titre="Certified Lover Boy", image="https://i.scdn.co/image/ab67616d0000b273cd945b4e3de57edd28481a3f", 
              date_sortie=timezone.make_aware(datetime(2021, 9, 3)), artiste=Artiste.objects.get(nom="Drake")),
        Album(titre="Happier Than Ever", image="https://i.scdn.co/image/ab67616d0000b2732a038d3bf875d23e4aeaa84e", date_sortie=timezone.make_aware(datetime(2021, 7, 30)), artiste=Artiste.objects.get(nom="Billie Eilish")),
        Album(titre="=", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROM588AR5Q_FZL9_bfJ0O3BXOK7_vaIzKsVg&s", date_sortie=timezone.make_aware(datetime(2021, 10, 29)), artiste=Artiste.objects.get(nom="Ed Sheeran")),
        Album(titre="BE", image="https://i.scdn.co/image/ab67616d0000b273c07d5d2fdc02ae252fcd07e5", date_sortie=timezone.make_aware(datetime(2020, 11, 20)), artiste=Artiste.objects.get(nom="BTS")),
        Album(titre="30", image="https://i.scdn.co/image/ab67616d0000b273c6b577e4c4a6d326354a89f7", date_sortie=timezone.make_aware(datetime(2021, 11, 19)), artiste=Artiste.objects.get(nom="Adele"))
    ]
    Album.objects.bulk_create(albums_data)


# Datas morceaux
def create_morceaux():
    morceaux_data = [
        Morceau(titre="Anti-Hero", duree="00:03:21", 
                album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Lavender Haze", duree="00:03:22", 
                album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Maroon", duree="00:03:38", 
                album=Album.objects.get(titre="Midnights")),
        Morceau(titre="You're on Your Own, Kid", duree="00:03:14", 
                album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Midnight Rain", duree="00:02:54", 
                album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Way 2 Sexy", duree="00:04:18", 
                album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Happier Than Ever", duree="00:05:35", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="Shivers", duree="00:03:27", album=Album.objects.get(titre="=")),
        Morceau(titre="Life Goes On", duree="00:03:27", album=Album.objects.get(titre="BE")),
        Morceau(titre="Easy On Me", duree="00:03:44",album=Album.objects.get(titre="30"))
    ]
    Morceau.objects.bulk_create(morceaux_data)


# Datas morceaux/genres
def create_genre_morceaux():
    genre_morceaux_data = [
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Anti-Hero")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Way 2 Sexy")),
        GenreHasMorceau(genre=Genre.objects.get(titre="R&B"), morceau=Morceau.objects.get(titre="Happier Than Ever")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Shivers")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Life Goes On")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Easy On Me"))
    ]
    GenreHasMorceau.objects.bulk_create(genre_morceaux_data)

def create_datas():
    create_artistes()
    create_genres()
    create_albums()
    create_morceaux()
    create_genre_morceaux()
    print("Les données ont été créées avec succès !")


if __name__ == "__main__":
    create_datas()
