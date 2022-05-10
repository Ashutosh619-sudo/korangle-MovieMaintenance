from rest_framework import serializers
from .models import Actor, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Actor
        fields = "__all__"