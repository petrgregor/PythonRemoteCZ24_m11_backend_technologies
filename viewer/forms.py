from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea, ModelForm, NumberInput

from viewer.models import Country, Creator

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
