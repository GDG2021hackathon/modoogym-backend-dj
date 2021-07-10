from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class MyUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email')
        read_only_fields = ('email',)
