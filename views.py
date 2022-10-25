from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from flask import request
from itsdangerous import Serializer
from .models import Employee   

# Employee Functions
@login_required(login_url='login')
def employee_list(request):
    employee_list = Employee.objects.all()
    e = {'employee_list':employee_list}
    return render(request,'employee.html', e)

def delete_employee(request,id):
    em = Employee.objects.get(id=id).delete()
    return redirect('employee_list')

def edit_employee(request,id):
    em = Employee.objects.get(id=id)
    if request.method=='POST':
        eid_ = request.POST.get('eid')
        ename_ = request.POST.get('ename')
        ephn_ = request.POST.get('ephn')
        esalary_ = request.POST.get('esalary')
        print('eid_')
        print('ename_')
        print('ephn_')
        print('esalary_')
        em.eid = eid_
        em.ename = ename_
        em.ephn = ephn_
        em.esalary = esalary_
        em.save()
        return redirect('employee_list')
    else:
        e = {'em':em}
        return render(request,'edit.html',e)

def add_employee(request):
    if request.method=='POST':
        eid_ = request.POST.get('eid')
        ename_ = request.POST.get('ename')
        ephn_ = request.POST.get('ephn')
        esalary_ = request.POST.get('esalary')
        print('eid_')
        print('ename_')
        print('ephn_')
        print('esalary_')
        Employee.objects.create(eid = eid_, ename = ename_, ephn = ephn_, esalary = esalary_)
        return redirect('employee_list')
    else:
        return render(request,'edit.html')

