from rest_framework import serializers

from notes.models import Note
from content.api.serializers import ContentCourseListSerializer

class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'title',
            'body',
            'type',
            'free',
            'price',
        )


class NoteListSerializer(serializers.ModelSerializer):
    contents = ContentCourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'type',
            'free',
            'price',
            'contents',
        )


class NoteSerializer(serializers.ModelSerializer):
    contents = ContentCourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'type',
            'free',
            'price',
            'contents',
        )
