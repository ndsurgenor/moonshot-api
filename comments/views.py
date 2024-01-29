from rest_framework import generics, permissions
from moonshot_api.permissions import IsPermittedOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    GET and POST functionality for Comments
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT and DELETE functionality for Comments
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = Comment.objects.all()
