from rest_framework import serializers
from .models import Star


class StarSerializer(serializers.ModelSerializer):
    """
    Converts Star model data to JSON
    """
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Star
        fields = [
            'id',
            'user',
            'photo',
            'created_at',
            'value,'
        ]