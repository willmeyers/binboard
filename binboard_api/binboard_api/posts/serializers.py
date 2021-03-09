from rest_framework import serializers

from users.serializers import PublicUserSerializer
from tags.models import Tag
from tags.serializers import TagSerializer
from .models import Post


class PublicPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    url = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'user',
            'url',
            'title',
            'description',
            'created_at',
            'updated_at',
            'tags'
        ]


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
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'user'
            'url',
            'title',
            'description',
            'replace',
            'shared',
            'starred',
            'toread',
            'created_at',
            'updated_at',
            'tags'
        ]


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

    def create(self, validated_data):
        tag_titles = validated_data.pop('tags')

        if request.user and request.user.is_authenticated():
            validated_data['user'] = request.user

        post = Post.objects.create(**validated_data)

        if tag_titles:
            tag_titles = tag_titles.split()

            tags = []
            for tag in tag_titles:
                tags.append(Tag(**{
                    'title': tag,
                    'is_private': True if tag.startswith('.') else False
                    'content_object': post,
                    'object_id': post.id
                }))

            Tags.objects.bulk_create(tags)
        
        return post
