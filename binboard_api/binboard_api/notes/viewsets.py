from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post
from tags.models import Tag
from .models import Note
from .serializers import PublicNoteSerializer, UserNoteSerializer


class PublicNoteViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Note.objects.all()
        serializer = PublicNoteSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Note.objects.all()

        note = get_object_or_404(queryset, pk=pk)
        serializer = PublicNoteSerializer(note)

        return Response(serializer.data)


class UserNoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = UserNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        data = serializer.data

        note = Note.objects.create(**data)

        post = Post.objects.create(

        )

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

        return note
