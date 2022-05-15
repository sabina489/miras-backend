from rest_framework.generics import (ListAPIView,)
from rest_framework.permissions import (AllowAny,)
from rest_framework.response import Response
from content.api.serializers import (
    ContentListSerializer,
    ContentCourseListSerializer,
)
from content.models import Content
from courses.models import Course


# class ContentListAPIView(ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ContentListSerializer
#     queryset = Content.objects.all()


# class ContentCourseListAPIView(ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ContentCourseListSerializer
#     queryset = Content.objects.all()

#     def get_queryset(self):
#         return super().get_queryset().filter(course__id=self.kwargs['course_id'])

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         course = Course.objects.get(id=self.kwargs['course_id'])
#         data = {'free': []}
#         for part in course.parts.all():
#             data[part.name] = []

#         for content in serializer.data:
#             if content['part']:
#                 data[content['part']['name']].append(content)
#             else:
#                 data['free'].append(content)

#         return Response(data)


# class ContentCoursePartListAPIView(ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ContentCourseListSerializer
#     queryset = Content.objects.all()

#     def get_queryset(self):
#         return super().get_queryset().filter(course__id=self.kwargs['course_id'], part__id=self.kwargs['part_id'])
