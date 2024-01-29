from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """
    Converts Photo model data to JSON
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source="user.user_profile.id")
    user_avatar = serializers.ReadOnlyField(source="user.user_profile.avatar.url")

    # Ensures photo upload is less than 2MB in size
    # and height/width are between 500-4096px 
    def validate_photo(self, value):
        size = value.size
        height = value.image.height
        width = value.image.width

        if size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image file size must be less than 2MB'
                )
        if height < 500 or height > 4096:
            raise serializers.ValidationError(
                'Image height must be between 500-4096 pixels'
                )
        if width < 500 or width > 4096:
            raise serializers.ValidationError(
                'Image width must be between 500-4096 pixels'
                ) 
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    class Meta:
        model = Photo
        fields = [
            'id',
            'user',
            'is_owner',
            'user_id',
            'user_avatar',
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