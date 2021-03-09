from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import PublicPostSerializer, UserPostSerializer


class PublicPostsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PublicPostSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        
        post = get_object_or_404(queryset, pk=pk)
        serializer = PublicPostSerializer(post)

        return Response(serializer.data)

    @action(detail=False)
    def popular(self, request):
        queryset = Post.objects.all()
        serializer = PublicPostSerializer(queryset, many=True)

        return Response(serializer.data)

    @action(detail=False)
    def recent(self, request):
        queryset = Post.objects.all()
        serializer = PublicPostSerializer(queryset, many=True)

        return Response(serializer.data)


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