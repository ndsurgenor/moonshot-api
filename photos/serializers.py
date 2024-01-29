from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    " Converts Photo model data to JSON "
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    user_profile_id = serializers.ReadOnlyField(source="user.user_profile.id")
    user_profile_avatar = serializers.ReadOnlyField(source="user.user_profile.avatar.url")

    #Ensures photo upload is less than 2MB in size and height/width are under 4096px 
    def validate_photo(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image file size must be less than 2MB')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height must be less than 4096 pixels')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width must be less than 4096 pixels')
        return value


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