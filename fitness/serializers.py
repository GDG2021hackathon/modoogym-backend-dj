from rest_framework import serializers

from .models import Fitness


class FitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = ["id"]
