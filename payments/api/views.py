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
)
from payments.models import (
    Payment,
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

class OnlinePaymentUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OnlinePaymentUpdateSerializer
    queryset = OnlinePayment.objects.all()