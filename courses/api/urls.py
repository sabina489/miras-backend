from django.urls import path

from courses.api.views import (
    CourseListAPIView,
    CourseRequestCreateAPIView,
    CourseRequestListAPIView,
    CourseRequestViewCountAPIView,
    CourseRequestVoteAPIView,
    CourseRetrieveAPIView,
    CourseCategoryListAPIView,
    CourseCategoryRetrieveAPIView,
)

urlpatterns = [
    path('get/<int:pk>/', CourseRetrieveAPIView.as_view(), name='retrieve'),
    path('list/<int:catid>/', CourseListAPIView.as_view(), name='course-list'),
    path('list/', CourseListAPIView.as_view(), name='course-list-all'),
    path('categories/', CourseCategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>', CourseCategoryRetrieveAPIView.as_view(),
         name='category-retrieve'),
]


urlpatterns += [
    path('request/create/', CourseRequestCreateAPIView.as_view(), name='request-create'),
    path('request/list/', CourseRequestListAPIView.as_view(), name='request-list'),
    path('request/vote/<int:pk>/', CourseRequestVoteAPIView.as_view(), name='request-vote'),
    path('request/view/<int:pk>/', CourseRequestViewCountAPIView.as_view(), name='request-view'),
]
