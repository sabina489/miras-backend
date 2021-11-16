from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model
from accounts.api.permissions import OwnObjectPermission

from accounts.api.serializers import UserCreateSerializer, UserUpdateSerializer, UserRetrieveSerializer


User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, OwnObjectPermission]
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, OwnObjectPermission]
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.all()


class UserProfileAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, OwnObjectPermission]
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
