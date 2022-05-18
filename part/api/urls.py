from django.urls import path, re_path
from part.api.views import (
    PartListAPIView,
    PartRetrieveAPIView,
)

urlpatterns = [
    path('<int:pk>/', PartRetrieveAPIView.as_view(), name='part-retrieve'),
    # re_path('^list/(?P<classid>.+)/$', PartListAPIView.as_view()),
    path('list/<int:classid>/', PartListAPIView.as_view(), name='part-list'),
    # path('', PartListAPIView.as_view(), name='list'),
]
