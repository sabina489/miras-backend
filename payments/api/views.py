from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from notes.api import serializers
from payments.api.serializers import (
    OnlinePaymentCreateSerializer,
    OnlinePaymentUpdateSerializer,
    BankPaymentCreateSerializer,
)
from payments.models import (
    BankPayment,
    OnlinePayment
)

# class PaymentCreateAPIView(CreateAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = PaymentCreateSerializer
#     queryset = Payment.objects.all()


class OnlinePaymentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OnlinePaymentCreateSerializer
    queryset = OnlinePayment.objects.all()


class BankPaymentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BankPaymentCreateSerializer
    queryset = BankPayment.objects.all()


class OnlinePaymentUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OnlinePaymentUpdateSerializer
    queryset = OnlinePayment.objects.all()
