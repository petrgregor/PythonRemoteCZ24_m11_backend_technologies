# Generated by Django 5.1.3 on 2024-12-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
