from rest_framework import serializers

from .models import Post

class PublicPostSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'description',
            'created_at',
            'updated_at'
        ]


class UserPostSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    replace = serializers.BooleanField(write_only=True)
    shared = serializers.BooleanField()
    starred = serializers.BooleanField()
    toread = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'description',
            'replace',
            'shared',
            'starred',
            'toread',
            'created_at',
            'updated_at'
        ]
