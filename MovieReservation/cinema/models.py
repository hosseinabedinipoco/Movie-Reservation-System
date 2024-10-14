from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField()
    Address = models.CharField(max_length=100)
    rate = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.name
    
class Seat(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    row = models.PositiveSmallIntegerField()
    number = models.PositiveIntegerField()
    
    def __str__(self):
        return self.cinema + ", " + self.row +", " + self.number
