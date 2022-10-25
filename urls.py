from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    path('employee_list', views.employee_list, name='employee_list'),
    path('delete_employee/<int:id>', views.delete_employee, name='delete_employee'),
    path('edit_employee/<int:id>', views.edit_employee, name='edit_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
]
