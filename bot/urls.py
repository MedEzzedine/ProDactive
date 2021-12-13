from django.urls import path
from .views import *

urlpatterns = [
    #path("employee/", EmployeeAPIView.as_view()),
    path("employee/", allEmployees),
    path("absentemployees/", checkAbsenceByDay),
    path("employee/<int:id>/inbox/", checkInbox),
    path("employee/add-justification", addAbsenceJustification)
]