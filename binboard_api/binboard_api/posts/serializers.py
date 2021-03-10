from rest_framework import serializers

from tags.serializers import TagSerializer
from .models import Post


class PublicPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    url = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    created_ago = serializers.CharField()
    count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'user',
            'url',
            'title',
            'description',
            'created_ago',
            'count',
            'tags'
        ]
    
    def get_count(self, obj):
        return Post.objects.filter(url=obj.url).count()


class UserPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    url = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    replace = serializers.BooleanField(write_only=True)
    shared = serializers.BooleanField()
    starred = serializers.BooleanField()
    toread = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'user',
            'url',
            'title',
            'description',
            'replace',
            'shared',
            'starred',
            'toread',
            'created_at',
            'updated_at',
            'count',
            'tags'
        ]
    
    def get_count(self, obj):
        return Post.objects.filter(url=obj.url).count()


class CreatePostSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    shared = serializers.BooleanField()
    toread = serializers.BooleanField()
    tags = serializers.CharField()

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'description',
            'shared',
            'toread',
            'tags'
        ]
