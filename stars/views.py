from rest_framework import generics, permissions
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import Star
from .serializers import StarSerializer


class StarList(generics.ListCreateAPIView):
    """
    GET and POST functionality for Stars
    """
    serializer_class = StarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Star.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT and DELETE functionality for Stars
    """
    serializer_class = StarSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = Star.objects.all()