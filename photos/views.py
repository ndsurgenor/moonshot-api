from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer
from moonshot_api.permissions import IsPermittedOrReadOnly


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


class PhotoDetail(APIView):
    """
    Displays the details of an individual photo
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsPermittedOrReadOnly]

    # Check permissions
    def get_object(self, pk):
        try:
            photo = Photo.objects.get(pk=pk)
            self.check_object_permissions(self.request, photo)
            return photo
        except Photo.DoesNotExist:
            raise Http404
    
    # GET functionality
    def get(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(
            photo,
            context={'request': request},
        )
        return Response(serializer.data)
    
    # PUT functionality
    def put(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(
            photo,
            data=request.data,
            context={'request': request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # DELETE functionality
    def put(self, request, pk):
        photo = self.get_object(pk)
        photo.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )