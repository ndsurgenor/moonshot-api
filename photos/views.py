from django.db.models import Count
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
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'created_at',
        'star_count',
        'comment_count',
    ]

    def link_photo_with_user(self, serializer):
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