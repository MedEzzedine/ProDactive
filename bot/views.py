from datetime import date
from django.shortcuts import render

from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse

#from celery.schedules import crontab
#from celery.task import periodic_task

#import requests

# Create your views here.

"""class EmployeeAPIView(APIView):

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


@api_view(["GET"])
def allEmployees(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

"""def collectData(request):
    response = requests.get("https://prodactive-botapi-test.herokuapp.com/employee/")
    print(response.text)"""
@api_view(["POST"])
def checkAbsenceByDay(request):
    serializer = AbsentEmployeesSerializer(data=request.data)
    if serializer.is_valid():
        for id in serializer.data["absentEmployees"]:
            emp = Employee.objects.get(pk = id)
            emp.absence_set.create(date=serializer.data["date"])
            emp.monthlyScore-=1
            emp.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

