from django.urls import path
from . import views
urlpatterns = [
    path('add', views.Add_Show.as_view()),
    path('update/<int:id>', views.Update_Show.as_view()),
    path('delete/<int:id>', views.Delete_Show.as_view()),
    path('get_all', views.Get_All_Show.as_view()),
    path('get/<int:id>', views.Get_Show.as_view()),
]
