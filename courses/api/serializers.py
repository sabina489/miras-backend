from django.db.models import fields
from rest_framework import serializers

from courses.models import Course, CourseCategory, CourseRequest, CourseStatus
from enrollments.api.utils import count_enrollments, is_enrolled, is_enrolled_active
from part.api.serializers import (
    PartSerializer,
    PartRetrieveSerializer,
)
from notes.api.serializers import NoteSerializer
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
    notes = NoteSerializer(many=True)
    exams_exam_related = ExamSerializer(many=True,)

    def to_representation(self, instance):
        """Count the number of course enrollments."""
        count = 0
        for part in instance.parts.all():
            count += count_enrollments(part)
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
            'requester_name',
            'requester_email',
            'requester_phone',
        )


class CourseRequestVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRequest
        fields = ("vote_count",)


class CourseRequestViewCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRequest
        fields = ("view_count",)


class CourseRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRequest
        fields = (
            'id',
            'course_name',
            'course_category',
            'status',
            'vote_count',
            'view_count',
            'created_at',
        )