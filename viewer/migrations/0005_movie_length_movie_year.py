# Generated by Django 5.1.3 on 2024-11-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_alter_country_options_creator_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]