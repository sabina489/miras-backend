from django.urls import path

from courses.api.views import (
    CourseListAPIView,
    CourseRetrieveAPIView,
    CourseCategoryListAPIView,
    CourseCategoryRetrieveAPIView,
)

urlpatterns = [
    path('get/<int:pk>/', CourseRetrieveAPIView.as_view(), name='retrieve'),
    path('get/', CourseListAPIView.as_view(), name='course-list'),
    path('categories/', CourseCategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>', CourseCategoryRetrieveAPIView.as_view(),
         name='category-retrieve')
]
