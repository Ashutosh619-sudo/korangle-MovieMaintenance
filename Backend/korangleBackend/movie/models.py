from django.db import models

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=500, unique=True, blank=False)
    description = models.TextField(max_length=1500)
    release_date = models.DateField(blank=False)
    no_of_actors = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:

        return self.title

class Actor(models.Model):

    name = models.CharField(max_length=100,blank=False)
    date_of_birth = models.DateField(blank=False)
    no_of_movies = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class MovieActor(models.Model):

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        self.movie.no_of_actors += 1
        self.movie.save()
        self.actor.no_of_movies += 1
        self.actor.save()
        super(MovieActor,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.movie)+ " => " + str(self.actor)
