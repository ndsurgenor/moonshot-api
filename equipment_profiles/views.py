from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import EquipmentProfile
from .serializers import EquipmentProfileSerializer


class EquipmentProfileList(generics.ListAPIView):
    """
    GET functionality for Equipment Profiles
    """
    serializer_class = EquipmentProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = EquipmentProfile.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = [
        'user__username',
        'main_lens',
        'main_camera',
        'other_equipment',
    ]
    filterset_fields = [
        'user',
    ]
    ordering_fields = [
        'created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EquipmentProfileDetail(generics.RetrieveUpdateAPIView):
    """
    PUT functionality for Equipment Profiles
    """
    serializer_class = EquipmentProfileSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = EquipmentProfile.objects.all()
