from rest_framework import serializers

from location.serializers import LocationSerializer
from .models import Membership


class MembershipSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="fitness.name", read_only=True)
    seller_nickname = serializers.CharField(source="seller.nickname", read_only=True)
    image = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()

    class Meta:
        model = Membership
        fields = ["id", "title", "price", "end_date", "description", "image", "like", "fitness", "name",
                  "seller", "seller_nickname"]
        read_only_fields = ["seller"]

    def get_image(self, membership):
        return membership.fitness.sub_image

    def get_like(self, membership):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        if membership in self.context.get('request').user.favorites.all():
            return True
        else:
            return False


class MyMembershipSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="fitness.name", read_only=True)
    location = LocationSerializer(source="fitness.location", read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Membership
        fields = ["id", "title", "price", "validation", "end_date", "description", "image", "fitness", "name",
                  "location"]
        read_only_fields = ["validation"]

    def get_image(self, membership):
        return membership.fitness.sub_image
