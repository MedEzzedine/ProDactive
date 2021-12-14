from rest_framework import serializers
from .models import *

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'
        depth = 1

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 1

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = ['firstName', 'lastName', 'email', 'grade', 'score', 'inscriptionDate']
        fields = '__all__'


class AbsentEmployeesSerializer(serializers.Serializer):
    date = serializers.DateField()
    absentEmployees = serializers.ListField(child=serializers.IntegerField())

class justificationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    justification = serializers.URLField()
    
#SUPERVISOR
class ModeratedAbsencesSerializer(serializers.Serializer):
    validatedAbsences = serializers.ListField(child = serializers.IntegerField())
    rejectedAbsences = serializers.ListField(child = serializers.IntegerField())


