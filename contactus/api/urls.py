from django.urls import path
from contactus.api.views import ContactUsAPIView


urlpatterns = [
    path('', ContactUsAPIView.as_view(), name="contact_us_create"),
]
