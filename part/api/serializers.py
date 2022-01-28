from rest_framework import serializers
from content.api.serializers import ContentCourseListSerializer
from enrollments.models import EnrollmentStatus

from part.models import Part
from enrollments.api.utils import count_enrollments, is_enrolled, is_enrolled_active
from notes.api.serializers import NoteSerializer


class PartRetrieveSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()
    is_enrolled_active = serializers.SerializerMethodField()
    notes = NoteSerializer(many=True)

    class Meta:
        model = Part
        fields = (
            "id",
            "name",
            "course",
            "detail",
            "price",
            "count",
            "is_enrolled",
            "is_enrolled_active",
            "notes",
        )

    def get_count(self, obj):
        """
        Get the number of enrollments for the part.
        obj: Part object
        """
        return count_enrollments(obj)

    def get_is_enrolled(self, obj):
        return is_enrolled(obj, self.context["request"].user)

    def get_is_enrolled_active(self, obj):
        """
        Get the enrollment status of the user for the part.
        obj: Part object
        """
        return is_enrolled_active(obj, self.context["request"].user)


class PartSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Part
        fields = (
            "id",
            "name",
            "price",
            "detail",
            "notes"
        )
