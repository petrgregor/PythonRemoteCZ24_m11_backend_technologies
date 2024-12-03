import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea, ModelForm, NumberInput

from viewer.models import Country, Creator, Genre, Movie, Review, Image

"""
class CreatorForm(Form):
    first_name = CharField(max_length=32, required=False)
    last_name = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    nationality = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)
"""


class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        #fields = ['biography', 'first_name', 'last_name']
        #exclude = ['nationality']
        labels = {
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'nationality': 'Národnost',
            'biography': "Biografie"
        }
        help_texts = {
            'biography': "Zde zadejte biografii tvůrce."
        }
        error_messages = {
            # TODO
        }

    #first_name = CharField(max_length=32, required=False, label='Jméno')
    #last_name = CharField(max_length=32, required=False, label='Příjmení')
    date_of_birth = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}), label='Datum narození')
    date_of_death = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}), label='Datum úmrtí')

    #nationality = ModelChoiceField(queryset=Country.objects, required=False, label='Národnost')
    #biography = CharField(widget=Textarea, required=False, label="Biografie")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_first_name(self):
        """ Upraví zadané jméno tak, aby začínalo velkým písmenem. """
        initial = self.cleaned_data['first_name']
        print(f"Initial = '{initial}'")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result  = '{result}'")
        return result

    def clean_last_name(self):
        """ Upraví zadané příjmení tak, aby začínalo velkým písmenem. """
        initial = self.cleaned_data['last_name']
        print(f"Initial = '{initial}'")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result  = '{result}'")
        return result

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        print(f"Initial = '{initial}'")
        if initial and initial > date.today():
            raise ValidationError("Lze zadávat datum narození pouze v minulosti.")
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        print(f"Initial = '{initial}'")
        if initial and initial > date.today():
            raise ValidationError("Lze zadávat datum úmrtí pouze v minulosti.")
        return initial

    def clean_biography(self):
        # Force each sentence of the biography to be capitalized.
        initial = self.cleaned_data['biography']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        initial_first_name = cleaned_data['first_name']
        initial_last_name = cleaned_data['last_name']
        print(f"initial_first_name = '{initial_first_name}', initial_last_name = '{initial_last_name}'")
        if not initial_first_name and not initial_last_name:
            raise ValidationError("Je potřeba zadat jméno nebo příjmení (nebo oboje).")

        initial_date_of_birth = cleaned_data.get('date_of_birth')
        initial_date_of_death = cleaned_data.get('date_of_death')
        if initial_date_of_birth and initial_date_of_death and initial_date_of_death <= initial_date_of_birth:
            raise ValidationError("Datum úmrtí nemůže být dřív, než datum narození.")

        return cleaned_data


class GenreModelForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            name = name.strip()
            name = name.capitalize()
        return name


class CountryModelForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            name = name.strip()
            name = name.capitalize()
        return name


class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title_orig', 'title_cz', 'year', 'length', 'directors', 'actors', 'countries', 'genres',
                  'description']
        labels = {
            'title_orig': 'Originální název',
            'title_cz': 'Český název',
            'year': 'Rok',
            'length': 'Délka (min)',
            'directors': 'Režie',
            'actors': 'Herecké obsazení',
            'countries': 'Země',
            'genres': 'Žánry',
            'description': 'Popis',
        }
        help_texts = {
            'title_orig': 'Zadajte originální název filmu.',
            'title_cz': 'Zadajte český název filmu (pokud existuje).',
            'year': 'Zadajte rok vydání filmu.',
            'length': 'Délka filmu v minutách.',
            'description': 'Popis filmu, stručný obsah nebo jiné detaily.',
        }
        error_messages = {
            'title_orig': {
                'required': 'Tento údaj je povinný.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_title_orig(self):
        title_orig = self.cleaned_data['title_orig']
        if title_orig:
            title_orig = title_orig.strip()
            title_orig = title_orig.capitalize()
        return title_orig

    def clean_title_cz(self):
        title_cz = self.cleaned_data['title_cz']
        if title_cz:
            title_cz = title_cz.strip()
            title_cz = title_cz.capitalize()
        return title_cz

    def clean_year(self):
        year = self.cleaned_data['year']
        if year and year > date.today().year:
            raise ValidationError("Rok filmu nemůže být v budoucnosti.")
        return year

    def clean_length(self):
        length = self.cleaned_data['length']
        if length and length <= 0:
            raise ValidationError("Déžka filmu musí být větší než 0.")
        return length

    def clean(self):
        cleaned_data = super().clean()

        title_orig = cleaned_data.get('title_orig')
        if not title_orig:
            raise ValidationError("Originální název je povinný.")

        return cleaned_data


class ReviewModelForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Hodnocení',
            'comment': 'Komentář'
        }


class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {
            'image': 'Obrázek',
            'movie': 'Film',
            'actors': 'Herci',
            'description': 'Popis'
        }
