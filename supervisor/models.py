from django.db import models

# Create your models here.

class Absence(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    justification = models.ImageField(upload_to='pdf', null=True, blank=True, default='')
    valid = models.BooleanField(default=False)

    def __str__(self):
        return f"Employee Absent on day {self.date}"

class Message(models.Model):
    type = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} Message"

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    grade = models.IntegerField(default=1)
    monthlyScore = models.IntegerField(default=30)
    absenceCollection = models.ForeignKey(Absence, on_delete=models.CASCADE, null=True, blank=True, default='')
    messageCollection = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True, default='')
    inscriptionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Employee {self.firstName.title()} {self.lastName.title()}"