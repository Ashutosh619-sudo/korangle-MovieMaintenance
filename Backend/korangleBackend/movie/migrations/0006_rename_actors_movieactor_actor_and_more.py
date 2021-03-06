# Generated by Django 4.0.4 on 2022-05-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_movie_no_of_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieactor',
            old_name='actors',
            new_name='actor',
        ),
        migrations.AlterField(
            model_name='actor',
            name='number_of_movies',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='no_of_actors',
            field=models.IntegerField(blank=True),
        ),
    ]
