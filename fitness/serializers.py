from rest_framework import serializers

from category.serializers import CategorySerializer
from location.serializers import LocationSerializer
from .models import Fitness


class FitnessSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = LocationSerializer()

    class Meta:
        model = Fitness
        fields = ["id", "name", "navigation", "location", "category"]
