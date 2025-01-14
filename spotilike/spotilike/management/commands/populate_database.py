# spotilike/management/commands/populate_database.py

from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils import timezone
from spotilike.models import Artiste, Genre, Morceau, GenreHasMorceau, Album

class Command(BaseCommand):
    help = 'Peuple la base de données avec des artistes, genres, albums, et morceaux'

    def handle(self, *args, **kwargs):
        # Création des artistes
        artistes_data = [
            Artiste(nom="Taylor Swift", avatar="https://example.com/taylor_swift_avatar.jpg", biographie="Taylor Swift est une auteure-compositrice-interprète américaine, célèbre pour ses chansons mélodiques et ses paroles évocatrices."),
            Artiste(nom="Drake", avatar="https://example.com/drake_avatar.jpg", biographie="Drake est un rappeur, chanteur et producteur canadien, connu pour sa polyvalence musicale et ses collaborations internationales."),
            Artiste(nom="Billie Eilish", avatar="https://example.com/billie_eilish_avatar.jpg", biographie="Billie Eilish est une artiste américaine au style unique, mêlant pop alternative et influences sombres."),
            Artiste(nom="Ed Sheeran", avatar="https://example.com/ed_sheeran_avatar.jpg", biographie="Ed Sheeran est un chanteur et compositeur britannique, célèbre pour ses ballades romantiques et ses performances acoustiques."),
            Artiste(nom="BTS", avatar="https://example.com/bts_avatar.jpg", biographie="BTS est un groupe de K-pop sud-coréen qui a conquis le monde avec ses chansons percutantes et ses chorégraphies impressionnantes."),
            Artiste(nom="Adele", avatar="https://example.com/adele_avatar.jpg", biographie="Adele est une chanteuse britannique reconnue pour sa voix puissante et ses ballades émouvantes."),
            Artiste(nom="Post Malone", avatar="https://example.com/post_malone_avatar.jpg", biographie="Post Malone est un rappeur et chanteur américain, connu pour ses chansons mêlant rap, pop et rock."),
            Artiste(nom="The Weeknd", avatar="https://example.com/the_weeknd_avatar.jpg", biographie="The Weeknd est un artiste canadien qui mélange R&B, pop et sonorités électroniques dans ses hits internationaux."),
            Artiste(nom="Dua Lipa", avatar="https://example.com/dua_lipa_avatar.jpg", biographie="Dua Lipa est une chanteuse britannique, connue pour ses tubes pop dansants et son style distinctif."),
            Artiste(nom="Bad Bunny", avatar="https://example.com/bad_bunny_avatar.jpg", biographie="Bad Bunny est un chanteur portoricain, pionnier de la musique reggaeton et trap latino.")
        ]
        Artiste.objects.bulk_create(artistes_data)

        # Création des genres
        genres_data = [
            Genre(titre="Pop", description="Un genre musical populaire, accessible et entraînant."),
            Genre(titre="Hip-Hop", description="Un genre rythmique, souvent lié à la culture urbaine."),
            Genre(titre="R&B", description="Un style mélodique, souvent axé sur les émotions."),
            Genre(titre="K-Pop", description="Un style musical sud-coréen combinant pop, rap et danse."),
            Genre(titre="Rock", description="Un genre énergique, influencé par les guitares électriques."),
            Genre(titre="Electro", description="Un genre basé sur des sons électroniques et des rythmes dansants.")
        ]
        Genre.objects.bulk_create(genres_data)

        # Création des albums
        albums_data = [
            Album(titre="Midnights", image="https://example.com/midnights.jpg", date_sortie=timezone.make_aware(datetime(2022, 10, 21)), artiste=Artiste.objects.get(nom="Taylor Swift")),
            Album(titre="Certified Lover Boy", image="https://example.com/certified_lover_boy.jpg", date_sortie=timezone.make_aware(datetime(2021, 9, 3)), artiste=Artiste.objects.get(nom="Drake")),
            Album(titre="Happier Than Ever", image="https://example.com/happier_than_ever.jpg", date_sortie=timezone.make_aware(datetime(2021, 7, 30)), artiste=Artiste.objects.get(nom="Billie Eilish")),
            Album(titre="=", image="https://example.com/equals.jpg", date_sortie=timezone.make_aware(datetime(2021, 10, 29)), artiste=Artiste.objects.get(nom="Ed Sheeran")),
            Album(titre="BE", image="https://example.com/be.jpg", date_sortie=timezone.make_aware(datetime(2020, 11, 20)), artiste=Artiste.objects.get(nom="BTS")),
            Album(titre="30", image="https://example.com/30.jpg", date_sortie=timezone.make_aware(datetime(2021, 11, 19)), artiste=Artiste.objects.get(nom="Adele"))
        ]
        Album.objects.bulk_create(albums_data)

        # Création des morceaux
        morceaux_data = [
            Morceau(titre="Anti-Hero", duree="00:03:21", morceau="anti_hero.mp3", album=Album.objects.get(titre="Midnights")),
            Morceau(titre="Way 2 Sexy", duree="00:04:18", morceau="way_2_sexy.mp3", album=Album.objects.get(titre="Certified Lover Boy")),
            Morceau(titre="Happier Than Ever", duree="00:05:35", morceau="happier_than_ever.mp3", album=Album.objects.get(titre="Happier Than Ever")),
            Morceau(titre="Shivers", duree="00:03:27", morceau="shivers.mp3", album=Album.objects.get(titre="=")),
            Morceau(titre="Life Goes On", duree="00:03:27", morceau="life_goes_on.mp3", album=Album.objects.get(titre="BE")),
            Morceau(titre="Easy On Me", duree="00:03:44", morceau="easy_on_me.mp3", album=Album.objects.get(titre="30"))
        ]
        Morceau.objects.bulk_create(morceaux_data)

        # Association des morceaux aux genres
        genre_morceaux_data = [
            GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Anti-Hero")),
            GenreHasMorceau(genre=Genre.objects.get(titre="Hip-Hop"), morceau=Morceau.objects.get(titre="Way 2 Sexy")),
            GenreHasMorceau(genre=Genre.objects.get(titre="R&B"), morceau=Morceau.objects.get(titre="Happier Than Ever")),
            GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Shivers")),
            GenreHasMorceau(genre=Genre.objects.get(titre="K-Pop"), morceau=Morceau.objects.get(titre="Life Goes On")),
            GenreHasMorceau(genre=Genre.objects.get(titre="Pop"), morceau=Morceau.objects.get(titre="Easy On Me"))
        ]
        GenreHasMorceau.objects.bulk_create(genre_morceaux_data)

        self.stdout.write(self.style.SUCCESS('Base de données peuplée avec succès !'))
