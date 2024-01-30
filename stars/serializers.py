from django.db import IntegrityError
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
            'value',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'Info': 'possible attempt at unpermitted duplicate'
            })