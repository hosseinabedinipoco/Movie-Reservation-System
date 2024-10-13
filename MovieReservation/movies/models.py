from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    time_in_minute = models.PositiveIntegerField()
    genre = models.CharField(max_length=10, default="")
    rate = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])


    def __str__(self):
        return self.title