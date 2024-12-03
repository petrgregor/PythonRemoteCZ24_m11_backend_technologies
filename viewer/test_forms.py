from unittest import skip

from django.test import TestCase

from viewer.forms import CreatorForm, MovieModelForm
from viewer.models import *


class CreatorFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(name="Česká republika")
        Country.objects.create(name="Slovenská republika")
        Country.objects.create(name="Německo")

    def test_creator_form_is_valid(self):
        form = CreatorForm(
            data={
                'first_name': '    martin    ',
                'last_name': '   novák   ',
                'date_of_birth': '1965-09-17',
                'date_of_death': '2022-10-10',
                'nationality': '1',
                'biography': 'Nějaký text.'
            }
        )
        self.assertTrue(form.is_valid())

    #@skip("Nefunguje datum narození v budoucnosti - domácí úkol")
    def test_creator_form_date_of_birth_is_invalid(self):
        form = CreatorForm(
            data={
                'first_name': '    martin    ',
                'last_name': '   novák   ',
                'date_of_birth': '2065-09-17',
                'date_of_death': '',
                'nationality': '1',
                'biography': 'Nějaký text.'
            }
        )
        self.assertFalse(form.is_valid())

    def test_creator_form_date_of_birth_date_of_death_is_invalid(self):
        form = CreatorForm(
            data={
                'first_name': '    martin    ',
                'last_name': '   novák   ',
                'date_of_birth': '2000-09-17',
                'date_of_death': '1995-05-03',
                'nationality': '1',
                'biography': 'Nějaký text.'
            }
        )
        self.assertFalse(form.is_valid())

    def test_creator_form_first_name_is_valid(self):
        form = CreatorForm(
            data={
                'first_name': '',
                'last_name': '   novák   ',
                'date_of_birth': '1955-09-17',
                'date_of_death': '1995-05-03',
                'nationality': '1',
                'biography': 'Nějaký text.'
            }
        )
        self.assertTrue(form.is_valid())

    def test_creator_form_last_name_is_valid(self):
        form = CreatorForm(
            data={
                'first_name': 'Bohumil',
                'last_name': '',
                'date_of_birth': '1955-09-17',
                'date_of_death': '1995-05-03',
                'nationality': '1',
                'biography': 'Nějaký text.'
            }
        )
        self.assertTrue(form.is_valid())

    def test_creator_form_name_is_invalid(self):
        form = CreatorForm(
            data={
                'first_name': '',
                'last_name': '',
                'date_of_birth': '1955-09-17',
                'date_of_death': '1995-05-03',
                'nationality': '1',
                'biography': 'Nějaký text.'
            }
        )
        self.assertFalse(form.is_valid())


class MovieFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        country_cz = Country.objects.create(name="Česká republika")
        country_sk = Country.objects.create(name="Slovenská republika")
        genre_drama = Genre.objects.create(name="Drama")
        genre_crime = Genre.objects.create(name="Krimi")

    def test_movie_form_is_valid(self):
        form = MovieModelForm(
            data={
                'title_orig': 'Samotáři',
                'title_cz': '',
                'year': '2000',
                'length': '135',
                'countries': ['1', '2'],  # pro vazbu ManyToMany zadáváme jako seznam
                'genres': ['1', '2']
            }
        )
        self.assertTrue(form.is_valid())

    def test_movie_form_year_is_invalid(self):
        form = MovieModelForm(
            data={
                'title_orig': 'Samotáři',
                'title_cz': '',
                'year': '2030',
                'length': '135',
                'countries': ['1', '2'],  # pro vazbu ManyToMany zadáváme jako seznam
                'genres': ['1', '2']
            }
        )
        self.assertFalse(form.is_valid())
