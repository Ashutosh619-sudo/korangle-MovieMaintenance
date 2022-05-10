from . import views
from django.urls import path

urlpatterns = [
    path('', view=views.get_all_movies),
    path('get-actors',view=views.get_actor_list),
    path('upvote',view=views.upvote_movie),
    path('downvote',view=views.downvote_movie),
]
