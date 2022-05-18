from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from enrollments.permissions import IsEnrolledActive
from notes.models import Note
from notes.api.serializers import (
    NoteListSerializer,
    NoteCreateSerializer
)


# class NoteCreateAPIView(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = NoteCreateSerializer
#     queryset = Note.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)


class NoteListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()


class NoteRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()


class NoteCourseListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        return self.queryset.filter(courses__id=self.kwargs['course_id'])
