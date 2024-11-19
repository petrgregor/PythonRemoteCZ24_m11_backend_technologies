from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea

from viewer.models import Country


class CreatorForm(Form):
    first_name = CharField(max_length=32, required=False)
    last_name = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    nationality = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)
