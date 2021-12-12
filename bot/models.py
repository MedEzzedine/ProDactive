from django.db import models
# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    grade = models.IntegerField(default=1)
    monthlyScore = models.IntegerField(default=30)
    yearlyScore = models.IntegerField(default=365)
    inscriptionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Employee {self.firstName.title()} {self.lastName.title()}"

class Absence(models.Model):
    date = models.DateField()
    justification = models.ImageField(upload_to='pdf', null=True, blank=True, default='')
    valid = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, default='')

    def __str__(self):
        return f"Employee Absent on day {self.date}"

class Message(models.Model):
    class MessageTypes(models.TextChoices):
        Warning = 'WARNING'
        Promotion = 'PROMOTION'
        Fired = 'FIRED'

    type = models.CharField(
        max_length=9,
        choices=MessageTypes.choices,
        default=MessageTypes.Warning,
    )
    content = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    Employees = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, default='')

    def __str__(self):
        return f"{self.type} Message"

