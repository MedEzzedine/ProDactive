from django.urls import path
from .views import *

urlpatterns = [
    path('employee/', EmployeeAPIView.as_view()),
]