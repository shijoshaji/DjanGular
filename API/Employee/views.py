import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Employees,Departments
from .serializer import EmployeeSerialiser,DepartmentSerialiser

@csrf_exempt
def department_api(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        department_serial = DepartmentSerialiser(departments,many=True)
        return JsonResponse(department_serial.data,safe=False)
    elif request.method=='POST':
        department_data =JSONParser().parse(request)
        department_serial=DepartmentSerialiser(data=department_data)
        if department_serial.is_valid():
            department_serial.save()
            return JsonResponse('Created New Record',safe=False)
        return JsonResponse('Failed to create a new Record',safe=False)
    elif request.method=='PUT':
        department_data =JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serial=DepartmentSerialiser(department,data=department_data)
        if department_serial.is_valid():
            department_serial.save()
            return JsonResponse('Updated Record',safe=False)
        return JsonResponse('Failed to Update Record',safe=False)
    elif request.method=='DELETE':
        department_data=Departments.objects.get(DepartmentId=id)
        department_data.delete()
        return JsonResponse('Record Deleted',safe=False)
        
        
@csrf_exempt
def employee_api(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employee_serial = EmployeeSerialiser(employees,many=True)
        return JsonResponse(employee_serial.data,safe=False)
    elif request.method=='POST':
        employee_data =JSONParser().parse(request)
        employee_serial=EmployeeSerialiser(data=employee_data)
        if employee_serial.is_valid():
            employee_serial.save()
            return JsonResponse('Created New Record',safe=False)
        return JsonResponse('Failed to create a new Record',safe=False)
    elif request.method=='PUT':
        employee_data =JSONParser().parse(request)
        employee = Employees.objects.get(EmpId=employee_data['EmpId'])
        employee_serial=EmployeeSerialiser(employee,data=employee_data)
        if employee_serial.is_valid():
            employee_serial.save()
            return JsonResponse('Updated Record',safe=False)
        return JsonResponse('Failed to Update Record',safe=False)
    elif request.method=='DELETE':
        employee_data=Employees.objects.get(EmpId=id)
        employee_data.delete()
        return JsonResponse('Record Deleted',safe=False)
    