import datetime
from unittest import skip

from django.test import TestCase

from viewer.models import *


class ViewerModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title_orig="Originální název filmu",
            title_cz="Český název filmu",
            year=2020,
            length=123,
            description="Popis filmu"
        )

        country_cz = Country.objects.create(
            name="Česká republika"
        )
        country_sk = Country.objects.create(
            name="Slovenská republika"
        )
        movie.countries.add(country_cz)
        movie.countries.add(country_sk)
        movie.countries.add(country_cz)

        genre_drama = Genre.objects.create(
            name="Drama"
        )
        genre_comedy = Genre.objects.create(
            name="Komedie"
        )
        movie.genres.add(genre_drama)
        movie.genres.add(genre_comedy)

        director = Creator.objects.create(
            first_name="Arnošt",
            last_name="Novák",
            date_of_birth=datetime.date(1975, 12, 10),
            nationality=country_cz,
            biography="Režisér několika filmů."
        )
        movie.directors.add(director)

        actor1 = Creator.objects.create(
            first_name="Bedřich",
            last_name="Svoboda",
            date_of_birth=datetime.date(1955, 9, 5),
            date_of_death=datetime.date(2023, 1, 5),
            nationality=country_cz,
            biography="Skvělý herec."
        )

        actor2 = Creator.objects.create(
            first_name="Cyril",
            last_name="Novotný",
            date_of_birth=datetime.date(1980, 2, 1),
            nationality=country_cz,
            biography="Slavný herec."
        )
        movie.actors.add(actor1)
        movie.actors.add(actor2)

        movie.save()

    def setUp(self):
        print('-'*80)

    def test_title_orig(self):
        movie = Movie.objects.get(id=1)
        print(f"test_title_orig: '{movie.title_orig}'")
        self.assertEqual(movie.title_orig, "Originální název filmu")

    def test_movie_str(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.__str__(), "Originální název filmu (2020)")

    def test_countries_count(self):
        movie = Movie.objects.get(id=1)
        countries_count = movie.countries.count()
        self.assertEqual(countries_count, 2)

    def test_length_format(self):
        movie = Movie.objects.get(id=1)
        length_format = movie.length_format()
        self.assertEqual(length_format, "2:03")  # 123 min

        movie.length = None
        movie.save()
        self.assertEqual(movie.length_format(), "neznámá")

        movie.length = 3
        movie.save()
        self.assertEqual(movie.length_format(), "0:03")

    def test_creator_full_name(self):
        director = Creator.objects.get(first_name="Arnošt", last_name="Novák")
        self.assertEqual(director.full_name(), "Arnošt Novák")

    @skip("Prozatím přeskočíme - domácí úloha")
    def test_creator_age(self):
        director = Creator.objects.get(first_name="Arnošt", last_name="Novák")
        self.assertEqual(director.age(), 48)

        director.date_of_birth = None
        director.date_of_death = None
        director.save()
        self.assertEqual(director.age(), None)

        director.date_of_birth = None
        director.date_of_death = datetime.date(2020, 1, 5)
        director.save()
        self.assertEqual(director.age(), None)

        director.date_of_birth = datetime.date(2000, 1, 29)
        director.date_of_death = None
        director.save()
        self.assertEqual(director.age(), 24)

        director.date_of_birth = datetime.date(2000, 1, 29)
        director.date_of_death = datetime.date(2024, 11, 26)
        director.save()
        self.assertEqual(director.age(), 24)

        director.date_of_birth = datetime.date(2000, 12, 29)
        director.date_of_death = datetime.date(2024, 11, 26)
        director.save()
        self.assertEqual(director.age(), 23)
