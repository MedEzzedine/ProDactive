from .models import *

def checkAbsenceByMonth():
    employees = Employee.objects.all()
    for emp in employees:
        if emp.monthlyScore <= 15:
            emp.message_set.create(type='FIRED',
                                   content=f"""Bonjour {emp.firstName.title()} {emp.lastName.title()},\nMalheureusement vous êtes viré de notre société""")
            #emp.delete()
            continue
        emp.monthlyScore = 30
        emp.save()

def checkAbsenceByYear():
    employees = Employee.objects.all()
    for emp in employees:
        if emp.yearlyScore >= 340:
            emp.grade += 1
            emp.message_set.create(type='PROMOTION',
                                   content=f"""Félicitations {emp.firstName.title()} {emp.lastName.title()}, vous êtes promu à un poste supérieur\n\tGrade: {emp.grade}""")
        emp.yearlyScore = 365
        emp.monthlyScore = 30
        emp.save()