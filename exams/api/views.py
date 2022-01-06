# TODO: make a mock test visible

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from enrollments.permissions import IsEnrolledActive

from .serializers import (
    ExamSerializer,
    MockExamSerializer,
    MCQExamSerializer,
    GorkhapatraExamSerializer,
    ExamStatusUpdateSerializer,
    ExamStatusRetrieveSerializer,
)
from ..models import (
    Exam,
    MockExam,
    MCQExam,
    GorkhapatraExam,
    # QuestionStatus,
)
from enrollments.models import (
    ExamStatus
)


class ExamListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class MockExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = MockExamSerializer
    queryset = MockExam.objects.all()


class MCQExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = MCQExamSerializer
    queryset = MCQExam.objects.all()


class GorkhaPatraExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = GorkhapatraExamSerializer
    queryset = GorkhapatraExam.objects.all()


# class QuestionStatusCreateAPIView(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = QuestionStatusCreateSerializer
#     queryset = QuestionStatus.objects.all()

#     def get_serializer(self, *args, **kwargs):
#         if isinstance(kwargs.get("data", {}), list):
#             kwargs["many"] = True
#         return super().get_serializer(*args, **kwargs)
class ExamStatusUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamStatusUpdateSerializer
    queryset = ExamStatus.objects.all()
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     exam_id = self.kwargs['examid']
    #     return queryset.filter(student=self.request.user)


class ExamStatusRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamStatusRetrieveSerializer
    queryset = ExamStatus.objects.all()

# class QuestionStatusRetrieveAPIView(RetrieveAPIView):
#     permission_classes = [AllowAny]
#     # [IsAuthenticated, IsEnrolled]
#     serializer_class = QuestionStatusSerializer
#     queryset = QuestionStatus.objects.all()
