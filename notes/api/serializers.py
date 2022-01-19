from rest_framework import serializers

from notes.models import Note


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'title',
            'body',
            'type',
            'file',
            'free',
            'price',
        )


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'type',
            'file',
            'free',
            'price',
        )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'type',
            'free',
            'price',
        )
