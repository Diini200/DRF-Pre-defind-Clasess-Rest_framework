from rest_framework.serializers import ModelSerializer
from testApp.models import Employee

class EmployeeSerialzer(ModelSerializer):
    class Meta:
        model =Employee
        fields= '__all__'