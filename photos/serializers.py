from rest_framework import serializers
from stars.models import Star
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """
    Converts Photo model data to JSON
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source='user.userprofile.id')
    user_avatar = serializers.ReadOnlyField(
        source='user.userprofile.avatar.url'
    )
    star_id = serializers.SerializerMethodField()
    star_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    # Ensures photo upload is less than 4MB in size
    # and height/width are between 500-7680px
    def validate_photo(self, value):
        size = value.size
        height = value.image.height
        width = value.image.width

        if size > 1024 * 1024 * 4:
            raise serializers.ValidationError(
                'Image file size must be less than 4MB'
                )
        if height < 500 or height > 7680:
            raise serializers.ValidationError(
                'Image height must be between 500-7680 pixels'
                )
        if width < 500 or width > 7680:
            raise serializers.ValidationError(
                'Image width must be between 500-7680 pixels'
                )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_star_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            star = Star.objects.filter(
                user=user,
                photo=obj,
            ).first()
            return star.id if star else None
        return None

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
            'photo_date',
            'photo_time',
            'lens_used',
            'camera_used',
            'other_equipment_used',
            'image',
            'star_id',
            'star_count',
            'comment_count',
        ]
