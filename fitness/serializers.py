from rest_framework import serializers

from category.serializers import CategorySerializer
from location.serializers import LocationSerializer
from membership.models import Membership
from .models import Fitness


class FitnessSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = LocationSerializer()
    counts = serializers.SerializerMethodField(default=0)

    class Meta:
        model = Fitness
        fields = ["id", "name", "score", "counts", "image", "navigation", "location", "category"]

    def get_counts(self, fitness):
        return len(Membership.objects.filter(fitness=fitness, validation=True))
