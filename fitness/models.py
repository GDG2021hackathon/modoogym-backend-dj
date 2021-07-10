from django.db import models


class Fitness(models.Model):
    name = models.CharField(max_length=20)
    score = models.FloatField()
    image = models.CharField(max_length=255)
    navigation = models.CharField(max_length=255)
    location = models.ForeignKey("location.Location", on_delete=models.CASCADE)
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "fitness"
