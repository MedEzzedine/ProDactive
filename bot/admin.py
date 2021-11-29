from django.contrib import admin
from .models import Employee, Absence, Message
# Register your models here.

admin.site.register(Employee)
admin.site.register(Absence)
admin.site.register(Message)