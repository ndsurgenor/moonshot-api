from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = [
            'user',
            'created_at',
            'updated_at',
            'name',
            'content',
            'avatar',
        ]