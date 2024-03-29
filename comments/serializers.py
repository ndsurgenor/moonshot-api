from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Converts Comment model data to JSON
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source='user.userprofile.id')
    user_avatar = serializers.ReadOnlyField(source='user.userprofile.avatar.url')

    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'is_owner',
            'user_id',
            'user_avatar',
            'photo',
            'created_at',
            'updated_at',
            'content',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Inherits from CommentSerializer and links photo as ReadOnlyField
    """
    photo = serializers.ReadOnlyField(source='photo.id')