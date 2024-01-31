from rest_framework import serializers
from .models import EquipmentProfile


class EquipmentProfileSerializer(serializers.ModelSerializer):
    """
    Converts EquipmentProfile model data to JSON
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    class Meta:
        model = EquipmentProfile
        fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
            'lens',
            'camera',
            'other_equipment',
            'is_owner',
        ]