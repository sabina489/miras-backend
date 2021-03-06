from django.urls import path
from notes.api.views import (
    NoteCourseListAPIView,
    # NoteCreateAPIView,
    NoteListAPIView,
    NoteRetrieveAPIView,
)


urlpatterns = [
    # path('create/', NoteCreateAPIView.as_view(), name='create'),
    path('list/', NoteListAPIView.as_view(), name='list'),
    path('detail/<int:pk>/', NoteRetrieveAPIView.as_view(), name='detail'),
    path('course/<int:course_id>/', NoteCourseListAPIView.as_view(), name='course'),
]
