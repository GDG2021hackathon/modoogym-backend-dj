from rest_framework import serializers

from .models import Membership


class MembershipSerializer(serializers.ModelSerializer):
    fitness_name = serializers.CharField(source="fitness.name", read_only=True)
    seller_nickname = serializers.CharField(source="seller.nickname", read_only=True)

    class Meta:
        model = Membership
        fields = ["id", "price", "end_date", "description", "fitness", "fitness_name", "seller", "seller_nickname"]
        read_only_fields = ["seller"]


class MyMembershipSerializer(serializers.ModelSerializer):
    fitness_name = serializers.CharField(source="fitness.name", read_only=True)

    class Meta:
        model = Membership
        fields = ["id", "price", "validation", "end_date", "description", "fitness", "fitness_name"]
        read_only_fields = ["validation"]
