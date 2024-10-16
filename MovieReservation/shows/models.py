from django.db import models
from movies.models import Movie
from cinema.models import Cinema
# Create your models here.
class Show(models.Model):
    time = models.DateTimeField()
    cinema = models.ForeignKey(Cinema, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    price = models.IntegerField()

    def __str__(self):
        return self.movie + " in " + self.cinema + " at " + self.time

