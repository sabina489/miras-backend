from rest_framework import serializers

from notes.models import Note
from content.api.serializers import ContentCourseListSerializer
from common.api.mixin import EnrolledSerializerMixin


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'title',
            'body',
            'price',
        )


class NoteListSerializer(EnrolledSerializerMixin):

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'price',
            "is_enrolled",
            "is_enrolled_active",
        )


class NoteSerializer(EnrolledSerializerMixin):
    contents = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'price',
            'contents',
            "is_enrolled",
            "is_enrolled_active",
        )

    def get_contents(self, obj):
        if self.get_is_enrolled_active(obj):
            return ContentCourseListSerializer(obj.contents.all(), many=True).data
        return []
