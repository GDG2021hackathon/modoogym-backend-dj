from django.db import models

from fitness.models import Fitness
from user.models import User


class Membership(models.Model):
    price = models.IntegerField()
    validation = models.BooleanField(default=True)
    end_date = models.DateField()
    description = models.CharField(max_length=255)
    fitness = models.ForeignKey(Fitness, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "membership"
