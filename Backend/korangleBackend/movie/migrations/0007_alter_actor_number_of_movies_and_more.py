# Generated by Django 4.0.4 on 2022-05-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_rename_actors_movieactor_actor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='number_of_movies',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='no_of_actors',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
