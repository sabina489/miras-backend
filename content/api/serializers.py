from rest_framework.serializers import ModelSerializer
from content.models import Content
from part.api.serializers import PartSerializer

class ContentListSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'id', 
            'name', 
            'description', 
            'free', 
            'file',
            'course',
            'part',
        ]


class ContentCourseListSerializer(ModelSerializer):
    part = PartSerializer(read_only=True)
    
    class Meta:
        model = Content
        fields = [
            'id', 
            'name', 
            'description', 
            'free', 
            'file',
            'course',
            'part',
        ]