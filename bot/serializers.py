from rest_framework import serializers
from .models import *

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = ['firstName', 'lastName', 'email', 'grade', 'score', 'inscriptionDate']
        fields = '__all__'
        depth = 1

class AbsentEmployeesSerializer(serializers.Serializer):
    date = serializers.DateField()
    absentEmployees = serializers.ListField(child=serializers.IntegerField())
    
