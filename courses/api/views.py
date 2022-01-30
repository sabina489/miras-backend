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
)

from courses.models import (
    Course,
    CourseCategory,
    CourseRequest
)
from courses.api.serializers import (
    CourseRequestCreateSerializer,
    CourseRequestListSerializer,
    CourseRequestViewCountSerializer,
    CourseRequestVoteSerializer,
    CourseRetrieveSerializer,
    CourseCategoryRetrieveSerializer,
)


class CourseCreateAPIView(CreateAPIView):
    pass


class CourseUpdateAPIView(UpdateAPIView):
    pass


class CourseDeleteAPIView(DestroyAPIView):
    pass


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
    permission_classes = [AllowAny]
    serializer_class = CourseRequestCreateSerializer


class CourseRequestVoteAPIView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseRequestVoteSerializer
    queryset = CourseRequest.objects.all()

    def perform_update(self, serializer):
        serializer.save(vote_count=serializer.instance.vote_count + 1)


class CourseRequestViewCountAPIView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseRequestViewCountSerializer
    queryset = CourseRequest.objects.all()

    def perform_update(self, serializer):
        serializer.save(view_count=serializer.instance.view_count + 1)


class CourseRequestListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseRequestListSerializer
    queryset = CourseRequest.objects.all()
