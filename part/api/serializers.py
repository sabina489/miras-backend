from rest_framework import serializers

from part.models import Part
from enrollments.api.utils import count_enrollments

class PartRetrieveSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """Count the number of part enrollments."""
        ret =  super().to_representation(instance)
        ret['count'] = count_enrollments(instance)
        return ret
    class Meta:
        model = Part
        fields = (
            "id",
            "name",
            "course",
            "detail",
            "price"
        )
