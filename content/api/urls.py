from django.urls import path
from content.api.views import (
    ContentListAPIView,
    ContentCourseListAPIView,
    ContentCoursePartListAPIView
)

app_name = 'content'

urlpatterns = [
    # path('list/', ContentListAPIView.as_view(), name='list'),
    # path('course/<int:course_id>/',
    #      ContentCourseListAPIView.as_view(), name='course_list'),
    # path('course/<int:course_id>/part/<int:part_id>/',
    #      ContentCoursePartListAPIView.as_view(), name='course_part_list'),
]
