from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from tags.models import Tag
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

    def perform_create(self, serializer):
        data = serializer.data
        
        data['user'] = self.request.user
        
        post = Post.objects.create(**data)

        tags = data.pop('tags')
        if tags:
            tag_titles = tags.split()

            if tag_titles:
                tag_titles = tag_titles.split()

                tags = []
                for tag in tag_titles:
                    tags.append(Tag(**{
                        'title': tag,
                        'is_private': True if tag.startswith('.') else False,
                        'content_object': post,
                        'object_id': post.id
                    }))

                Tag.objects.bulk_create(tags)
        
        return post

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