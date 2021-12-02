from  rest_framework import filters
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
    IsAdminUser
)
from accounts.api import permissions

from courses.models import (
    Course,
    CourseCategory
)
from courses.api.serializers import (
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
        category_id = self.kwargs['catid']
        return queryset.filter(category=category_id)


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
