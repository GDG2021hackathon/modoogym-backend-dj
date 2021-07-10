from rest_framework import serializers

from category.serializers import CategorySerializer
from location.serializers import LocationSerializer
from membership.models import Membership
from .models import Fitness


class FitnessSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = LocationSerializer()
    count = serializers.SerializerMethodField(default=0)

    class Meta:
        model = Fitness
        fields = ["id", "name", "score", "count", "image", "navigation", "location", "category"]

    def get_count(self, fitness):
        return len(Membership.objects.filter(fitness=fitness, validation=True))
