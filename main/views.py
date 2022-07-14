from email import message
from re import I
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status
from main.models import Student
from main.serializers import StudentSerializer
# Create your views here.

@api_view(['POST'])
def addStudent(request):
    student = StudentSerializer(data=request.data)
  
    # validating for already existing data
    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if student.is_valid():
        student.save()
        return Response(student.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    




@api_view(('GET',))
def getAll(request):
    students = Student.objects.all()
    serialiser = StudentSerializer(students,many=True)
    return Response(serialiser.data)


@api_view(('GET',))
def getByClass(request):
    grade =request.GET.get("grade")
    print(grade)
    students = Student.objects.all().filter(grade=grade)
    serialiser = StudentSerializer(students,many=True)

    return Response(serialiser.data)

@api_view(('GET',))
def getBySection(request):
    section =request.GET.get("section")
 
    students = Student.objects.all().filter(section=section)
    serialiser = StudentSerializer(students,many=True)
    return Response(serialiser.data)





