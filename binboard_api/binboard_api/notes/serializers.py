from rest_framework import serializers


from tags.serializers import TagSerializer
from .models import Note


class PublicNoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    note = serializers.CharField()
    note_hash = serializers.CharField()
    created_ago = serializers.CharField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = [
            'title',
            'note',
            'note_hash',
            'created_ago',
            'tags'
        ]


class UserNoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    note = serializers.CharField()
    note_hash = serializers.CharField()
    shared = serializers.BooleanField()
    created_ago = serializers.CharField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = [
            'title',
            'note',
            'note_hash',
            'shared',
            'created_ago',
            'tags'
        ]