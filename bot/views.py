from datetime import date
from django.shortcuts import render

from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view  

import requests

# Create your views here.

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
            emp.message_set.create(type='WARNING',
                                   content=f"""Attention {emp.firstName.title()} {emp.lastName.title()},\n vous avez une absence non justifée le {serializer.data["date"]}""")
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
        absence_list = []
        for absence in absences:
            if absence.checked == False:
                absence_info = {
                    "id" : absence.id,
                    "date": absence.date ,
	                "justification": absence.justification,
                }
                absence_list.append(absence_info)
        if len(absence_list)!=0:
            json[emp.id] = absence_list
    return Response(json)

@api_view(["POST"])
def moderateJustification(request):
    serializer = ModeratedAbsencesSerializer(data=request.data)
    if serializer.is_valid():
        for validated_absence_id, rejected_absence_id in zip(serializer.data["validatedAbsences"],serializer.data["rejectedAbsences"]):
            validated_absence = Absence.objects.get(pk = validated_absence_id)
            rejected_absence = Absence.objects.get(pk = rejected_absence_id)
            validated_absence.checked = rejected_absence.checked = True
            validated_absence.valid = True
            validated_absence.save()
            rejected_absence.save()
            rejected_absence.employee.message_set.create(type = 'WARNING', content = f"Votre certificat d\'absence pour le {rejected_absence.date} n\'est pas valide.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
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
    #print(serializer.data["id"])
    if serializer.is_valid():
        absence = Absence.objects.get(pk=serializer.data["id"])
        absence.justification=serializer.data["justification"]
        absence.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)