from rest_framework import serializers

from enrollments.models import ExamStatus
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
    is_enrolled_active,
)


class ExamSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()
    is_enrolled_active = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = (
            'id',
            'name',
            'created_at',
            'kind',
            'count',
            'category',
            'price',
            'is_enrolled',
            'is_enrolled_active'
        )

    def get_count(self, obj):
        return count_enrollments(obj)

    def get_is_enrolled(self, obj):
        return is_enrolled(obj, self.context["request"].user)

    def get_is_enrolled_active(self, obj):
        return is_enrolled_active(obj, self.context["request"].user)


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
            'marks',
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


class EnrolledQuestionSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # data = data.filter(
        #     examinee = self.context['request'].user
        # )
        # data = data.latest('updated_at')
        # print('*******')
        # print(data)
        return super(EnrolledQuestionSerializer, self).to_representation(data)


class QuestionStateRetrieveSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer()
    selected_option = OptionSerializer()

    class Meta:
        model = QuestionStatus
        list_serializer_class = EnrolledQuestionSerializer
        fields = (
            # 'id',
            'question',
            'selected_option',
        )


class QuestionStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionStatus
        fields = (
            'id',
            'question',
            'selected_option',
        )


class ExamStatusUpdateSerializer(serializers.ModelSerializer):
    question_states = QuestionStateSerializer(many=True)

    class Meta:
        model = ExamStatus
        fields = (
            'question_states',
        )

    def update(self, instance, validated_data):
        question_states = validated_data.pop('question_states')

        for state_data in question_states:
            question = state_data["question"]
            option = state_data["selected_option"]
            prev_question_states = instance.question_states.all()
            prev_states = prev_question_states.filter(question=question)
            if len(prev_states) > 0:
                prev_state = prev_states.first()
                prev_state.question = question
                prev_option = prev_state.selected_option
                prev_state.selected_option = option
                prev_state.save()
                new_option = prev_state.selected_option
                if new_option.correct != prev_option.correct:
                    if new_option.correct:
                        instance.score += prev_state.question.marks
                    else:
                        instance.score -= prev_state.question.marks
            else:
                new_state = QuestionStatus(
                    exam_stat=instance,
                    question=question,
                    selected_option=option
                )
                new_state.save()
                if new_state.selected_option.correct == True:
                    instance.score += new_state.question.marks
        instance.save()
        return instance


class ExamStatusRetrieveSerializer(serializers.ModelSerializer):
    question_states = QuestionStateRetrieveSerializer(many=True)
    rank = serializers.SerializerMethodField()

    class Meta:
        model = ExamStatus
        fields = (
            'id',
            'enrollment',
            'exam',
            'question_states',
            'score',
            'rank',
        )

    def get_rank(self, obj):
        return ExamStatus.objects.filter(score__lte=obj.score).count()
