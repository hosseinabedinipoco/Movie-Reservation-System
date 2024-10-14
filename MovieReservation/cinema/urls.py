from django.urls import path
from . import views
urlpatterns = [
    path('add', views.Add_cinema.as_view()),
    path('update/<int:id>', views.Update_Cinema.as_view()),
    path('delete/<int:id>', views.delete_Cinema.as_view()),4
    path
]
