from django.db import models
from users.models import User
from shows.models import Show
# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.DO_NOTHING)
    seat_number = models.SmallIntegerField()

    def __str__(self):
        return self.user + " in " + self.show + " on seat " + self.seat_number