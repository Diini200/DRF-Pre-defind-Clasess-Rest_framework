from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_Number = models.IntegerField()
    emp_Name=models.CharField(max_length=64)
    emp_Email=models.EmailField()
    emp_Address= models.CharField(max_length= 164)
    
    
    