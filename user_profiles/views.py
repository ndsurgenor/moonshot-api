from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileList(APIView):
    """ List all user profiles"""
    def get(self, request):
        user_profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)

class UserProfileDetail(APIView):
    def get_object(self, pk):
        try:
            user_profile = UserProfile.objects.get(pk=pk)
            return user_profile
        except UserProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)