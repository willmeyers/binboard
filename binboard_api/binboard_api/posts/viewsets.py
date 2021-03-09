from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import PublicPostSerializer, UserPostSerializer


class ReadOnlyPostsViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PublicPostSerializer

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)

    @action(detail=False)
    def popular(self, request):
        pass

    @action(detail=False)
    def recent(self, request):
        pass

    @action(detail=False)
    def dates(self, request):
        pass

    @action(detail=False)
    def suggest(self, request):
        pass

    @action(detail=False)
    def all(self, request):
        pass


class UserPostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserPostSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)

    @action(detail=False)
    def popular(self, request):
        pass

    @action(detail=False)
    def recent(self, request):
        pass

    @action(detail=False)
    def dates(self, request):
        pass

    @action(detail=False)
    def suggest(self, request):
        pass

    @action(detail=False)
    def all(self, request):
        pass