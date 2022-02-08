from rest_framework import serializers
from content.api.serializers import RecordedVideoSerializer

from part.models import Part
from enrollments.api.utils import count_enrollments, is_enrolled, is_enrolled_active
from notes.api.serializers import (
    NoteSerializer,
    NoteListSerializer
)
from common.api.mixin import EnrolledSerializerMixin


class PartRetrieveSerializer(EnrolledSerializerMixin):

    count = serializers.SerializerMethodField()
    notes = NoteListSerializer(many=True)

    class Meta:
        model = Part
        fields = (
            "id",
            "name",
            "course",
            "detail",
            "price",
            "count",
            "notes",
            "is_enrolled",
            "is_enrolled_active",
        )

    def get_count(self, obj):
        """
        Get the number of enrollments for the part.
        obj: Part object
        """
        return count_enrollments(obj)


class PartSerializer(EnrolledSerializerMixin):
    notes = NoteSerializer(many=True)
    recorded_videos = serializers.SerializerMethodField()

    def get_recorded_videos(self, obj):
        if self.get_is_enrolled_active(obj):
            return RecordedVideoSerializer(obj.recorded_video.all(), many=True).data
        return []

    class Meta:
        model = Part
        fields = (
            "id",
            "name",
            "price",
            "detail",
            "notes",
            "recorded_videos",
            "is_enrolled",
            "is_enrolled_active",
        )
