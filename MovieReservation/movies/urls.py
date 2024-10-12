from django.urls import path
from . import views
urlpatterns = [
    path('add', views.add_movie.as_view()),
    path('update', views.update_movie.as_view()),
    path('delete', views.delete_movie.as_view())
]
