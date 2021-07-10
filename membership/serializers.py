from rest_framework import serializers

from .models import Membership


class MembershipSerializer(serializers.ModelSerializer):
    fitness_name = serializers.CharField(source="fitness.name", read_only=True)
    seller_nickname = serializers.CharField(source="seller.nickname", read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Membership
        fields = ["id", "title", "price", "end_date", "description", "image", "fitness", "fitness_name", "seller",
                  "seller_nickname"]
        read_only_fields = ["seller"]

    def get_image(self, membership):
        return membership.fitness.sub_image


class MyMembershipSerializer(serializers.ModelSerializer):
    fitness_name = serializers.CharField(source="fitness.name", read_only=True)

    class Meta:
        model = Membership
        fields = ["id", "title", "price", "validation", "end_date", "description", "fitness", "fitness_name"]
        read_only_fields = ["validation"]
