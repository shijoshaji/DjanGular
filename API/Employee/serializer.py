from rest_framework import serializers
from .models import Departments,Employees


class DepartmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields=('__all__')
        
        
class EmployeeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields=('__all__')