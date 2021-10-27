from django.urls import path

from accounts.api.views import UserCreateAPIView, UserUpdateAPIView


urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
]
