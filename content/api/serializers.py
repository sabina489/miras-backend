from rest_framework import serializers
from content.models import Content, RecordedVideo
# from part.api.serializers import PartSerializer


class ContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'id',
            'name',
            'description',
            'link',
            'note',
        ]


class ContentCourseListSerializer(serializers.ModelSerializer):
    # part = PartSerializer(read_only=True)
    # file = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = [
            'id',
            'name',
            'description',
            'link'
            # 'part',
        ]

    # def get_file(self, obj):
    #     request = self.context.get('request')
    #     if request.user.is_authenticated:
    #         return request.build_absolute_uri(obj.file.url)
    #     return None


class RecordedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedVideo
        fields = [
            'id',
            'name',
            'link',
            'professor_name',
            'date',
        ]
