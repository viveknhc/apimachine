from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serializers import employeeSerializer

class employeeList(APIView):
    def get(self,request):
        employee1 = Employee.objects.all()
        serializer = employeeSerializer(employee1, many=True)
        return Response(serializer.data)
    
    
   