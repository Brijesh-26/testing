from django.urls import path
from .views import TestAPIView

urlpatterns = [
    path('api', TestAPIView.as_view()),
]
