from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(APIView):
    """
    Lists all uploaded photos
    """
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(
            photos,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PhotoSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )