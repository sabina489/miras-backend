from rest_framework import permissions
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.permissions import (
    AllowAny,
)
from part.models import (
    Part
)
from part.api.serializers import (
    PartRetrieveSerializer
)


class PartListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PartRetrieveSerializer

    def get_queryset(self):
        queryset = Part.objects.all()
        class_id = self.kwargs['classid']
        return queryset.filter(course=class_id)


class PartRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PartRetrieveSerializer
    queryset = Part.objects.all()
