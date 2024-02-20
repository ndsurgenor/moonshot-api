from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    """
    GET and POST functionality for Photos
    """ 
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Photo.objects.annotate(
        star_count=Count('stars', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,      
    ]
    search_fields = [
        'user__username',
        'title',
        'main_feature',
        'description',
        'location',
    ]
    filterset_fields = [
        'user',
        'main_feature',
        'user__userprofile',
        'stars__user__userprofile',
        'comment__user__userprofile',
        'user__comment__user__userprofile',       
    ]
    ordering_fields = [
        'created_at',
        'star_count',
        'comment_count',
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT and DELETE functionality for Photos
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = Photo.objects.annotate(
        star_count=Count('stars', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_at')