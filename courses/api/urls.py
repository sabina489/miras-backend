from django.urls import path

from courses.api.views import (
    CourseListAPIView,
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
         name='category-retrieve')
]
