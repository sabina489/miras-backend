from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from notes.models import Note
from notes.api.serializers import (
    NoteListSerializer,
    NoteCreateSerializer
)


class NoteCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteCreateSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class NoteListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()


class NoteDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()