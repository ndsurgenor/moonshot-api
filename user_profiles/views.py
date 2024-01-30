from django.db.models import Count
from rest_framework import generics, filters
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileList(generics.ListAPIView):
    """
    GET functionality for User Profiles
    """    
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.annotate(
        photo_upload_count=Count('user__photo', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = [
        'created_at',
        'photo_upload_count'
    ]
    search_fields = [
        'user__username',
        'name',
    ]


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    """
    PUT functionality for User Profiles
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = UserProfile.objects.annotate(
        photo_upload_count=Count(
            'user__photo',
            distinct=True
        )
    ).order_by('-created_at')