# Generated by Django 4.0.4 on 2022-05-09 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_movie_actors_movieactors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='number_of_actors',
        ),
    ]
