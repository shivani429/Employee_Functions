from multiprocessing.dummy.connection import Client
from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'eid', 'ename' ,'ephn', 'esalary')
