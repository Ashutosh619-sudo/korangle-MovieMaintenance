from django.contrib import admin
from .models import Movie,Actor,MovieActor

# Register your models here.


admin.site.register(Actor)
admin.site.register(MovieActor)

class MovieAdmin(admin.ModelAdmin):

    readonly_fields = ('no_of_actors','votes',)

admin.site.register(Movie,MovieAdmin)