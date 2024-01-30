from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
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
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,      
    ]
    search_fields = [
        'user__username',
        'content',
    ]
    filterset_fields = [
        'user',
        'photo',      
    ]
    ordering_fields = [
        'created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT and DELETE functionality for Comments
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsPermittedOrReadOnly]
    queryset = Comment.objects.all()
