from django.contrib import admin

from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id', 'emp_Number', 'emp_Name', 'emp_Email', 'emp_Address']

admin.site.register(Employee, EmployeeAdmin)