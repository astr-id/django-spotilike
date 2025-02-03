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
        Artiste(nom="Drake", avatar="https://imageio.forbes.com/specials-images/imageserve/5ed578988b3c370006234c35/0x0.jpg?format=jpg&crop=1031,1031,x43,y49,safe&height=416&width=416&fit=bounds", 
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
        Genre(titre="Electro", description="Un genre basé sur des sons électroniques et des rythmes dansants."),
        Genre(titre="Synth-Pop", description="Un sous-genre de la pop avec des synthétiseurs."),
        Genre(titre="Indie Pop", description="Une variante indépendante et alternative de la pop."),
        Genre(titre="Electropop", description="Un mélange entre l'électro et la pop."),
        Genre(titre="Dark Pop", description="Un sous-genre de la pop aux sonorités sombres."),
        Genre(titre="Alternative Pop", description="Un sous-genre de la pop avec des influences alternatives."),
        Genre(titre="Alternative Rock", description="Un sous-genre du rock avec une approche plus expérimentale."),
        Genre(titre="Bossa Nova", description="Un genre musical brésilien influencé par le jazz."),
        Genre(titre="Trap", description="Un sous-genre du hip-hop avec des beats lourds."),
        Genre(titre="Pop Rock", description="Un mélange entre la pop et le rock."),
        Genre(titre="Indie Rock", description="Un sous-genre du rock avec des influences indépendantes."),
        Genre(titre="Soul", description="Un genre axé sur des voix puissantes et des émotions profondes."),
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
        Album(titre="30", image="https://i.scdn.co/image/ab67616d0000b273c6b577e4c4a6d326354a89f7", date_sortie=timezone.make_aware(datetime(2021, 11, 19)), artiste=Artiste.objects.get(nom="Adele")),
        Album(titre="The Most Beautiful Moment in Life", image="https://i.scdn.co/image/ab67616d0000b273c6dbc63cf145b4ff6bee3322", date_sortie=timezone.make_aware(datetime(2016, 5, 2)), artiste=Artiste.objects.get(nom="BTS"))
    ]
    Album.objects.bulk_create(albums_data)


# Datas morceaux
def create_morceaux():
    morceaux_data = [
        # Midnights 
        Morceau(titre="Lavender Haze", duree="00:03:22", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Maroon", duree="00:03:38", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Anti-Hero", duree="00:03:21", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Snow on the Beach", duree="00:04:16", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="You're on Your Own, Kid", duree="00:03:14", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Midnight Rain", duree="00:02:54", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Question...?", duree="00:03:30", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Vigilante Shit", duree="00:02:44", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Bejeweled", duree="00:03:14", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Labyrinth", duree="00:04:07", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Karma", duree="00:03:24", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Sweet Nothing", duree="00:03:08", album=Album.objects.get(titre="Midnights")),
        Morceau(titre="Mastermind", duree="00:03:11", album=Album.objects.get(titre="Midnights")),

        # Certified Lover Boy 
        Morceau(titre="Champagne Poetry", duree="00:05:36", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Papi’s Home", duree="00:02:58", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Girls Want Girls", duree="00:03:41", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="In The Bible", duree="00:04:56", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Love All", duree="00:03:48", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Fair Trade", duree="00:04:51", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Way 2 Sexy", duree="00:04:18", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="TSU", duree="00:05:08", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="N 2 Deep", duree="00:04:33", album=Album.objects.get(titre="Certified Lover Boy")),
        Morceau(titre="Pipe Down", duree="00:04:05", album=Album.objects.get(titre="Certified Lover Boy")),

        # Happier Than Ever 
        Morceau(titre="Getting Older", duree="00:04:04", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="I Didn’t Change My Number", duree="00:02:38", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="Billie Bossa Nova", duree="00:03:16", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="my future", duree="00:03:30", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="Oxytocin", duree="00:03:30", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="GOLDWING", duree="00:02:31", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="Lost Cause", duree="00:03:32", album=Album.objects.get(titre="Happier Than Ever")),
        Morceau(titre="Happier Than Ever", duree="00:05:35", album=Album.objects.get(titre="Happier Than Ever")),

        # = 
        Morceau(titre="Tides", duree="00:03:15", album=Album.objects.get(titre="=")),
        Morceau(titre="Shivers", duree="00:03:27", album=Album.objects.get(titre="=")),
        Morceau(titre="First Times", duree="00:03:05", album=Album.objects.get(titre="=")),
        Morceau(titre="Overpass Graffiti", duree="00:03:56", album=Album.objects.get(titre="=")),
        Morceau(titre="The Joker and the Queen", duree="00:03:05", album=Album.objects.get(titre="=")),
        Morceau(titre="Visiting Hours", duree="00:03:35", album=Album.objects.get(titre="=")),

        # BE 
        Morceau(titre="Life Goes On", duree="00:03:27", album=Album.objects.get(titre="BE")),
        Morceau(titre="Fly to My Room", duree="00:03:42", album=Album.objects.get(titre="BE")),
        Morceau(titre="Blue & Grey", duree="00:04:15", album=Album.objects.get(titre="BE")),
        Morceau(titre="Stay", duree="00:03:26", album=Album.objects.get(titre="BE")),
        Morceau(titre="Dynamite", duree="00:03:19", album=Album.objects.get(titre="BE")),

        # 30 
        Morceau(titre="Strangers by Nature", duree="00:03:02", album=Album.objects.get(titre="30")),
        Morceau(titre="Easy On Me", duree="00:03:44", album=Album.objects.get(titre="30")),
        Morceau(titre="My Little Love", duree="00:06:29", album=Album.objects.get(titre="30")),
        Morceau(titre="Cry Your Heart Out", duree="00:04:15", album=Album.objects.get(titre="30")),
        Morceau(titre="Oh My God", duree="00:03:45", album=Album.objects.get(titre="30")),
        Morceau(titre="I Drink Wine", duree="00:06:16", album=Album.objects.get(titre="30")),
   
        # The Most Beautiful Moment in Life
        Morceau(titre="Epilogue: Young Forever", duree="00:02:06", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="Fire", duree="00:04:55", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="Save ME", duree="00:03:16", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="I Need U", duree="00:03:30", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="Run", duree="00:03:57", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="Butterfly", duree="00:03:59", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="House of Cards", duree="00:03:47", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
        Morceau(titre="Love is Not Over", duree="00:03:41", album=Album.objects.get(titre="The Most Beautiful Moment in Life")),
    ]
    Morceau.objects.bulk_create(morceaux_data)

# Datas morceaux/genres
def create_genre_morceaux():
    genre_morceaux_data = [
        # Midnights
        GenreHasMorceau(genre=Genre.objects.get(titre="Synth-Pop"), morceau=Morceau.objects.get(titre="Lavender Haze")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Synth-Pop"), morceau=Morceau.objects.get(titre="Maroon")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Anti-Hero")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Pop"), morceau=Morceau.objects.get(titre="Snow on the Beach")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Pop"), morceau=Morceau.objects.get(titre="You're on Your Own, Kid")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Electropop"), morceau=Morceau.objects.get(titre="Midnight Rain")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Synth-Pop"), morceau=Morceau.objects.get(titre="Question...?")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Dark Pop"), morceau=Morceau.objects.get(titre="Vigilante Shit")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Bejeweled")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Pop"), morceau=Morceau.objects.get(titre="Labyrinth")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Electropop"), morceau=Morceau.objects.get(titre="Karma")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Pop"), morceau=Morceau.objects.get(titre="Sweet Nothing")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Mastermind")),

        # Certified Lover Boy 
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Champagne Poetry")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Papi’s Home")),
        GenreHasMorceau(genre=Genre.objects.get(titre="R&B"), morceau=Morceau.objects.get(titre="Girls Want Girls")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="In The Bible")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Love All")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Fair Trade")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Trap"), morceau=Morceau.objects.get(titre="Way 2 Sexy")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="TSU")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="N 2 Deep")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Pipe Down")),

        # Happier Than Ever 
        GenreHasMorceau(genre=Genre.objects.get(titre="Alternative Pop"), morceau=Morceau.objects.get(titre="Getting Older")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Electropop"), morceau=Morceau.objects.get(titre="I Didn’t Change My Number")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Bossa Nova"), morceau=Morceau.objects.get(titre="Billie Bossa Nova")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Pop"), morceau=Morceau.objects.get(titre="my future")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Dark Pop"), morceau=Morceau.objects.get(titre="Oxytocin")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Alternative Rock"), morceau=Morceau.objects.get(titre="GOLDWING")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Pop"), morceau=Morceau.objects.get(titre="Lost Cause")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Alternative Rock"), morceau=Morceau.objects.get(titre="Happier Than Ever")),

        # = 
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop Rock"), morceau=Morceau.objects.get(titre="Tides")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Shivers")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="First Times")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Indie Rock"), morceau=Morceau.objects.get(titre="Overpass Graffiti")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="The Joker and the Queen")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Visiting Hours")),

        # BE
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Life Goes On")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Fly to My Room")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Blue & Grey")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Stay")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Dynamite")),

        # 30 
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Strangers by Nature")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Easy On Me")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Soul"), morceau=Morceau.objects.get(titre="My Little Love")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Cry Your Heart Out")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Oh My God")),
        GenreHasMorceau(genre=Genre.objects.get(titre="Soul"), morceau=Morceau.objects.get(titre="I Drink Wine")),
    
        # The Most Beautiful Moment in Life
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Epilogue: Young Forever")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Fire")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Save ME")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="I Need U")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Run")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Butterfly")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="House of Cards")),
        GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Love is Not Over")),
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
