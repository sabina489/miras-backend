from rest_framework import serializers
from enrollments.api.utils import is_enrolled, is_enrolled_active


class EnrolledSerializerMixin(serializers.ModelSerializer):
    is_enrolled = serializers.SerializerMethodField()
    is_enrolled_active = serializers.SerializerMethodField()

    # (
    #     "is_enrolled",
    #     "is_enrolled_active",
    # )

    def get_is_enrolled(self, obj):
        return is_enrolled(obj, self.context["request"].user)

    def get_is_enrolled_active(self, obj):
        """
        Get the enrollment status of the user for the part.
        obj: Part object
        """
        return is_enrolled_active(obj, self.context["request"].user)
