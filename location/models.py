from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    class Meta:
        db_table = "location"
