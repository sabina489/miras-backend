from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.utils import timezone
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.api.permissions import OwnObjectPermission

from accounts.api.serializers import (
    UserActivateSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserRetrieveSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserActivateAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserActivateSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'uidb64'

    def get_object(self):
        filter_kwargs = {'pk': force_text(
            urlsafe_base64_decode(self.kwargs[self.lookup_url_kwarg]))}
        obj = get_object_or_404(self.queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance is not None and default_token_generator.check_token(instance, self.kwargs['token']):

            serializer = self.serializer_class(
                instance, data={'is_active': True}, partial=partial)
            token = get_tokens_for_user(instance)
            status = 200
        else:
            serializer = self.serializer_class(
                instance, data={}, partial=partial)
            token = {}
            status = 401

        serializer.is_valid(raise_exception=True)
        serializer.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(token, status)


class UserActivateOTPAPIView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserActivateSerializer
    queryset = User.objects.all()
    lookup_field = "phone"

    def perform_update(self, serializer):
        serializer.save(is_active=True, otp_expiry=timezone.now())


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
