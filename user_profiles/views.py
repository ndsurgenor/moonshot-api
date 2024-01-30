from rest_framework import generics
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileList(generics.ListAPIView):
    """
    GET functionality for User Profiles
    """    
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    """
    PUT functionality for User Profiles
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = UserProfile.objects.all()