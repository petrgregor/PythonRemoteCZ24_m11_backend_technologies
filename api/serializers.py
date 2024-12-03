from rest_framework import serializers

from viewer.models import Movie, Creator


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        #fields = ['title_orig', 'title_cz', 'year']
        fields = '__all__'


class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = '__all__'
