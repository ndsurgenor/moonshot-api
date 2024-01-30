from rest_framework import generics, permissions
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    """
    GET and POST functionality for Photos
    """ 
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Photo.objects.all()

    def link_photo_with_user(self, serializer):
        serializer.save(user=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT and DELETE functionality for Photos
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = Photo.objects.all()