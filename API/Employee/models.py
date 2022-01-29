from pyexpat import model
from django.db import models
from django.forms import CharField

# Create your models here.
class Departments(models.Model):    

    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.DepartmentName
    
    
class Employees(models.Model):
    
    EmpId = models.AutoField(primary_key=True)
    EmpName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DOJ = models.DateField(auto_now=False, auto_now_add=False)
    Avatar = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.EmpName

    
