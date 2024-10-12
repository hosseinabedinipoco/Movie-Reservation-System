from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    time_in_minute = models.PositiveIntegerField()
    

    def __str__(self):
        return self.title