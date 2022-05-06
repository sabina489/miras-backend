from rest_framework import serializers
from common.api.mixin import EnrolledSerializerMixin

from enrollments.models import ExamStatus
from ..models import (
    Exam,
    MockExam,
    MCQExam,
    GorkhapatraExam,
    Officer,
    Question,
    QuestionStatus,
    Option,
)
from enrollments.api.utils import (
    is_enrolled,
    count_enrollments,
    is_enrolled_active,
)

from .utils import (
    calculate_full_marks,
)


class ExamSerializer(EnrolledSerializerMixin):
    count = serializers.SerializerMethodField()

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
            'neg_marks',
        )


class MockExamSerializer(ExamSerializer):
    questions = QuestionSerializer(many=True)
    officer = serializers.SerializerMethodField()

    class Meta():
        model = MockExam
        fields = ExamSerializer.Meta.fields + (
            'timer',
            'questions',
            'officer',
            'level',
        )

    def get_officer(self, obj):
        return obj.officer.all().values_list('name', flat=True)


class MockExamMiniSerializer(ExamSerializer):
    full_marks = serializers.SerializerMethodField()
    officer = serializers.SerializerMethodField()
    
    class Meta():
        model = MockExam
        fields = ExamSerializer.Meta.fields + (
            'timer',
            'full_marks',
            'officer',
            'level',
        )

    def get_full_marks(self, obj):
        return calculate_full_marks(obj)

    def get_officer(self, obj):
        return obj.officer.all().values_list('name', flat=True)


class MCQExamSerializer(ExamSerializer):
    questions = QuestionSerializer(many=True)

    class Meta():
        model = MCQExam
        fields = ExamSerializer.Meta.fields + (
            'questions',
        )


class MCQExamMiniSerializer(ExamSerializer):
    full_marks = serializers.SerializerMethodField()

    class Meta():
        model = MCQExam
        fields = ExamSerializer.Meta.fields + (
            'full_marks',
        )

    def get_full_marks(self, obj):
        return calculate_full_marks(obj)


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
            'submitted',
        )

    def update(self, instance, validated_data):
        question_states = validated_data.pop('question_states')
        submitted = validated_data.get('submitted') or False

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
                        instance.score += (prev_state.question.marks +
                                           prev_state.question.neg_marks)
                    else:
                        instance.score -= (prev_state.question.marks +
                                           prev_state.question.neg_marks)
            else:
                new_state = QuestionStatus(
                    exam_stat=instance,
                    question=question,
                    selected_option=option
                )
                new_state.save()
                if new_state.selected_option.correct == True:
                    instance.score += new_state.question.marks
                else:
                    instance.score -= new_state.question.neg_marks
        instance.submitted = submitted
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
            'submitted',
        )

    def get_rank(self, obj):
        all_examinee_states = ExamStatus.objects.filter(exam=obj.exam)
        num_examinee = all_examinee_states.count()
        num_examinee_lower_score = all_examinee_states.filter(
            score__lt=obj.score).count()
        return num_examinee - num_examinee_lower_score
