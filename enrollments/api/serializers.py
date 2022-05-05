from multiprocessing import context
from xml.dom import ValidationErr
from rest_framework import serializers
from courses.api.serializers import CourseSerializer
from enrollments.api.utils import is_enrolled

from enrollments.models import (
    Enrollment,
    EnrollmentStatus,
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

    exams = ExamStatusSerializer(
        many=True, source='exam_states', required=False)

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
        user = self.context['request'].user
        parts = validated_data.get('parts')
        notes = validated_data.get('notes')
        total_price = 0.0
        if not (exams_data or parts or notes):
            raise serializers.ValidationError(
                "Atleast one fields should be non-empty.")

        def batch_is_enrolled_and_price(enrolled_objs):
            sum_price = 0.0
            for enrolled_obj in enrolled_objs:
                sum_price += float(enrolled_obj.price)
                if he_is_enrolled := is_enrolled(enrolled_obj, user):
                    raise serializers.ValidationError(
                        f"{user} is already enrolled into {enrolled_obj}")

            return sum_price

        if parts:
            total_price += batch_is_enrolled_and_price(parts)
        if notes:
            total_price += batch_is_enrolled_and_price(notes)
        if exams_data:
            exams = [data.get("exam") for data in exams_data]
            total_price += batch_is_enrolled_and_price(exams)
        enrollment = super().create(validated_data)

        if exams_data:
            for data in exams_data:
                exam = data.get("exam")
                ExamStatus(enrollment=enrollment, exam=exam).save()
        if total_price == 0.0:
            enrollment.status = EnrollmentStatus.ACTIVE
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
        notes_0 = obj.notes.first()
        if part_0:
            return CourseSerializer(part_0.course, context=self.context).data
        if notes_0:
            return CourseSerializer(notes_0.courses, context=self.context).data
        return None
