from django.db.models import fields
from rest_framework import serializers

from courses.models import Course, CourseCategory, CourseRequest, CourseStatus
from enrollments.api.utils import count_enrollments
from part.api.serializers import (
    PartSerializer,
    PartRetrieveSerializer,
)
from notes.api.serializers import NoteListSerializer
from exams.api.serializers import ExamSerializer
from common.api.mixin import EnrolledSerializerMixin


class CourseCreateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'name',
            'created_at',
            'category',
            'instructor',
            'link',
            'password',
            'status',
            'main_detail',
            'class_detail',
            'benefit_detail',
            'video',
        )
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        course = Course.objects.create(**validated_data)
        course.save()
        return course


class CourseRetrieveSerializer(EnrolledSerializerMixin):
    parts = PartRetrieveSerializer(many=True)
    notes = NoteListSerializer(many=True)
    exams_exam_related = ExamSerializer(many=True,)

    def to_representation(self, instance):
        """Count the number of course enrollments."""
        count = sum(count_enrollments(part) for part in instance.parts.all())
        ret = super().to_representation(instance)
        ret['count'] = count
        return ret

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'created_at',
            'category',
            'instructor',
            'link',
            'password',
            'status',
            'price',
            'main_detail',
            'class_detail',
            'benefit_detail',
            'video',
            'parts',
            'notes',
            'exams_exam_related',
            'is_enrolled',
            'is_enrolled_active',
        )


class CourseCategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = (
            'id',
            'name',
            'parent'
        )


class CourseSerializer(serializers.ModelSerializer):
    parts = PartSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'parts',
        )


class CourseRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRequest
        fields = (
            'course_name',
            'course_category',
        )


class CourseRequestVoteSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()

    class Meta:
        model = CourseRequest
        fields = ("vote_count",)

    def get_vote_count(self, obj):
        return obj.number_of_votes()


# class CourseRequestViewCountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseRequest
#         fields = ("view_count",)


class CourseRequestListSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()
    has_voted = serializers.SerializerMethodField()

    class Meta:
        model = CourseRequest
        fields = (
            'id',
            'course_name',
            'course_category',
            'status',
            'vote_count',
            'created_at',
            'created_by',
            'has_voted',
        )

    def get_vote_count(self, obj):
        return obj.number_of_votes()

    def get_has_voted(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.has_voted(user)
        return False
