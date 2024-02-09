from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Converts UserProfile model data to JSON
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    photo_upload_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
            'name',
            'details',
            'avatar',
            'is_owner',
            'photo_upload_count',            
        ]