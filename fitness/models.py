from django.db import models


class Fitness(models.Model):
    name = models.CharField(max_length=20)
    navigation = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "fitness"
