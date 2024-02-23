from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from testApp.serializers import EmployeeSerialzer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

#==== This is to list all records using APIViews =======
# class EmpModelListApiView(APIView):
#     def get(self, request, format=None):
#        qs= Employee.objects.all()
#        Serializer= EmployeeSerialzer(qs, many=True)
#        return Response(Serializer.data)


#==== This is to list all records using ListAPIView using the normal way =======
class EmpModelListApiView(ListAPIView):
        serializer_class= EmployeeSerialzer
        
        def get_queryset(self):
                qs = Employee.objects.all()
                name = self.request.GET.get('emp_Name')
                if name is not None:
                        qs = qs.filter(emp_Name__icontains=name)
                return qs
#==== This is to list all records using ListAPIView using predefined variables =======
class EmpModelListApiView(ListAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
   
class EmpModelCreateApiView(CreateAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
   
class EmpModelRetrieveApiView(RetrieveAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
        lookup_field= 'id'
        
class EmpModelUpdateApiView(UpdateAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
        lookup_field= 'id'
   
class EmpModelDistroyApiView(DestroyAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
        lookup_field= 'id'

class EmpModelistCreateApiView(ListCreateAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
   
class EmpModelRetriveUpdateApiView(RetrieveUpdateAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
        lookup_field= 'id'

class EmpModelRetriveDistroyApiView(RetrieveDestroyAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
        lookup_field= 'id'

class EmpModelRetriveUpdateDistroyApiView(RetrieveUpdateDestroyAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerialzer
        lookup_field= 'id'
