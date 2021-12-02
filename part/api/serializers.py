from rest_framework import serializers
from enrollments.models import EnrollmentStatus

from part.models import Part
from enrollments.api.utils import count_enrollments


class PartRetrieveSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()

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
        )

    def get_count(self, obj):
        return count_enrollments(obj)

    def get_is_enrolled(self, obj):
        enrollements = obj.enrolls.all().filter(
            student=self.context['request'].user, status=EnrollmentStatus.ACTIVE)
        if len(enrollements) > 0:
            return True
        return False


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Part
        fields = ("id", "name")
