from django.db.models import fields
from rest_framework import serializers

from courses.models import Course, CourseCategory, CourseStatus

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
            'detail',
            'detail1',
            'video',
        )
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        course = Course.objects.create(**validated_data)
        course.save()
        return course


class CourseRetrieveSerializer(serializers.ModelSerializer):
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
            'detail',
            'video'
        )

class CourseCategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = (
            'name',
            'parent'
        )