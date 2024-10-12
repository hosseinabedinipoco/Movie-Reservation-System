from django.urls import path
from . import views
urlpatterns = [
    path('add', views.add_movie.as_view()),
    path('update/<int:id>', views.update_movie.as_view()),
    path('delete/<int:id>', views.delete_movie.as_view())
]
