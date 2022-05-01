from django.urls import path

from accounts.api.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserProfileAPIView,
    UserActivateAPIView,
    UserActivateOTPAPIView,
    UserPasswordResetRequestAPIView,
    UserPasswordResetConfirmAPIView,
    UserResetPasswordOTPConfirmAPIView,
    UserSendOTP,
)


urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('otp/activate/<str:phone>/',
         UserActivateOTPAPIView.as_view(), name="opt-activate"),
    path('activate/<str:uidb64>/<str:token>/',
         UserActivateAPIView.as_view(), name='activate'),

    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('get/<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('reset-password/', UserPasswordResetRequestAPIView.as_view(),
         name='reset-password'),
    path('reset-password/confirm/',
         UserPasswordResetConfirmAPIView.as_view(), name='reset-password'),
    path('reset-password/otp-confirm/',
         UserResetPasswordOTPConfirmAPIView.as_view(), name='reset-password'),
    path('send-otp/', UserSendOTP.as_view(), name='send-otp'),
]
