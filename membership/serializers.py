from rest_framework import serializers

from .models import Membership


class MembershipSerializer(serializers.ModelSerializer):
    fitness_name = serializers.CharField(source="fitness.name", read_only=True)

    class Meta:
        model = Membership
        fields = ["id", "price", "validation", "end_date", "description", "fitness", "fitness_name", "user"]
        read_only_fields = ["user", "validation"]
