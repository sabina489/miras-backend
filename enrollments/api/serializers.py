from rest_framework import serializers
from courses.api.serializers import CourseSerializer

from enrollments.models import (
    Enrollment,
    ExamStatus,
)
from notes.models import Note
from part.api.serializers import PartSerializer
from exams.api.serializers import ExamSerializer
from notes.api.serializers import NoteSerializer

from part.models import Part
from exams.models import Exam


class ExamStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStatus
        fields = (
            'id',
            'exam',
        )

class ExamStatusListSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    class Meta:
        model = ExamStatus
        fields = (
            'id',
            'exam',
        )

class EnrollmentCreateSerializer(serializers.ModelSerializer):

    exams = ExamStatusSerializer(many=True, source='exam_states', required=False)

    class Meta:
        model = Enrollment
        fields = (
            'id',
            # 'student',
            'parts',
            'exams',
            'notes',
        )

    def create(self, validated_data):
        exams_data = validated_data.pop('exam_states', None)
        enrollment = super().create(validated_data)

        if exams_data:
            for data in exams_data:
                exam = data.get("exam")
                ExamStatus(enrollment=enrollment, exam=exam).save()
        enrollment.save()
        return enrollment


class EnrollmentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            'id',
            'status'
        )


class EnrollmentRetrieveSerializer(serializers.ModelSerializer):

    parts = PartSerializer(many=True)
    notes = NoteSerializer(many=True)
    exam_states = ExamStatusListSerializer(many=True)
    course = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = (
            'id',
            'student',
            'status',
            'parts',
            'exam_states',
            'notes',
            'course',
            'created_at',
        )

    def get_course(self, obj):
        """
        Get the course of the enrollment
        obj is the enrollment object
        """
        part_0 = obj.parts.first()
        if part_0:
            return CourseSerializer(part_0.course).data
        return None
