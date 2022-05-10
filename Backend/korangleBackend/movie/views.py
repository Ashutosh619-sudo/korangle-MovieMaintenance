from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Movie, MovieActor
from .serialiers import MovieSerializer, ActorSerializer
from rest_framework import status

# Create your views here.

@api_view(["GET"])
def get_all_movies(request):
    movie = Movie.objects.all()
    order_by_title = request.query_params.get('title', None)
    order_by_date = request.query_params.get('release', None)
    if(order_by_title):
        movie = movie.order_by("title")
    
    if(order_by_date):
        movie = movie.order_by("release_date")

    serializer = MovieSerializer(movie,many=True)

    return Response({"data":serializer.data},status.HTTP_200_OK)

@api_view(["GET"])
def get_actor_list(request):
    
    movie_id = request.query_params.get('id')
    movie = Movie.objects.get(id=movie_id)

    actors_id = MovieActor.objects.filter(movie=movie).values_list('actor',flat=True)
    actors = Actor.objects.filter(pk__in=actors_id)
    
    serialier = ActorSerializer(actors,many=True)
    return Response({"data":serialier.data},status.HTTP_200_OK)

@api_view(["POST"])
def upvote_movie(request):

    movie_id = request.data["id"]
    movie = Movie.objects.get(id=movie_id)
    movie.votes += 1
    movie.save()
    return Response({"ok":True},status=status.HTTP_200_OK)

@api_view(["POST"])
def downvote_movie(request):

    movie_id = request.data["id"]
    movie = Movie.objects.get(id=movie_id)
    movie.votes -= 1
    movie.save()
    return Response({"ok":True},status=status.HTTP_200_OK)