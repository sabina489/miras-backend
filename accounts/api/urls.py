from django.urls import path

from accounts.api.views import UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView


urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('get/<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
]
