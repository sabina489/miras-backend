from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from courses.models import (
    Course,
    CourseCategory,
    CourseRequest
)
from courses.api.serializers import (
    CourseRequestCreateSerializer,
    CourseRequestListSerializer,
    CourseRequestVoteSerializer,
    CourseRetrieveSerializer,
    CourseCategoryRetrieveSerializer,
)


class CourseListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseRetrieveSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Course.objects.all()
        category_id = self.kwargs.get('catid')
        if category_id:
            return queryset.filter(category=category_id)
        return queryset


class CourseRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseRetrieveSerializer
    queryset = Course.objects.all()


class CourseCategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseCategoryRetrieveSerializer
    queryset = CourseCategory.objects.all()


class CourseCategoryRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseCategoryRetrieveSerializer
    queryset = CourseCategory.objects.all()


class CourseRequestCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseRequestCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class CourseRequestVoteAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseRequestVoteSerializer
    queryset = CourseRequest.objects.all()

    def perform_update(self, serializer):
        serializer.save(voters=[self.request.user])


class CourseRequestListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseRequestListSerializer
    queryset = CourseRequest.objects.all()
