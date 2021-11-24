from rest_framework import serializers

from part.models import Part

class PartRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            "name",
            "course",
            "enrolls",
            "detail",
            "price"
        )
