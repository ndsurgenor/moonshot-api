from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    user_profile_id = serializers.ReadOnlyField(source="user.user_profile.id")
    user_profile_avatar = serializers.ReadOnlyField(source="user.user_profile.avatar.url")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'is_owner',
            'user_profile_id',
            'user_profile_avatar',
            'created_at',
            'updated_at',
            'title',
            'main_feature',
            'description',
            'location',
            'date_taken',
            'time_taken',
            'equipment',
            'image',
        ]