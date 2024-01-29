from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(APIView):
    """
    Lists all uploaded photos
    """
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(
            photos,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)