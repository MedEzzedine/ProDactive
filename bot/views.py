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



#SUPERVISOR#
@api_view(["GET"])
def getAbsentEmployees(request):
    json = dict()
    employees = Employee.objects.all()
    for emp in employees:
        absences = emp.absence_set.all()
        for absence in absences:
            print(absence)
            absence_list = list()
            if absence.checked == False:
                absence_info = {
                    "date": absence.date ,
	                "justification": absence.justification,
                }
                absence_list.append(absence_info)
        print(absence_list)
        if len(absence_list)!=0:
            json[emp.id] = absence_list
    return Response(json)
#Employee#
@api_view(["GET"])
def checkInbox(request,id):
    emp = Employee.objects.get(pk = id)
    messages = emp.message_set.all()
    message_list = list()
    for message in messages:
        message_info = {
            "type":message.type,
            "creationDate":message.creationDate,
	        "content":message.content
        }
        message_list.append(message_info)
    return Response(message_list)

@api_view(["POST"])
def addAbsenceJustification(request):
    serializer = justificationSerializer(data=request.data)
    print(serializer.data["id"])
    if serializer.is_valid():
        absence = Absence.objects.get(pk=serializer.data["id"])
        absence.justification=serializer.data["justification"]
        absence.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
