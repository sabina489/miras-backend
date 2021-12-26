from rest_framework import serializers
from ..models import (
    Exam,
    MockExam,
    MCQExam,
    GorkhapatraExam,
    Question,
    QuestionStatus,
    Option,
)
from enrollments.api.utils import (
    is_enrolled,
    count_enrollments,
)


class ExamSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = (
            'id',
            'name',
            'created_at',
            'kind',
            'count',
            'category',
            'is_enrolled',
        )

    def get_count(self, obj):
        return count_enrollments(obj)

    def get_is_enrolled(self, obj):
        return is_enrolled(obj, self.context["request"].user)


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            'id',
            'detail',
            'correct',
            'question',
            'feedback',
            'img',
        )


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'detail',
            'img',
            'exam',
            'options',
        )


class MockExamSerializer(ExamSerializer):
    questions = QuestionSerializer(many=True)

    class Meta():
        model = MockExam
        fields = ExamSerializer.Meta.fields + (
            'timer',
            'questions'
        )


class MCQExamSerializer(ExamSerializer):
    questions = QuestionSerializer(many=True)

    class Meta():
        model = MCQExam
        fields = ExamSerializer.Meta.fields + (
            'questions',
        )


class GorkhapatraExamSerializer(ExamSerializer):
    class Meta:
        model = GorkhapatraExam
        fields = ExamSerializer.Meta.fields + (
            'content',
        )


class QuestionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionStatus
        fields = (
            'id',
            'examinee',
            'question',
            'selected_option',
        )
