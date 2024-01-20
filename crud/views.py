from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .models import Student
from .models import Teacher
# Create your views here.

@api_view(['POST'])
def postStudent(request):
 try:
    request_data = request.data
    serializer = StudentSerializer(data=request_data , many=False)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message': 'Student added successfully'})
 except Exception as e:
        return Response(e)                
@api_view(['POST']) 
def postTeacher(request):
 try:
    request_data = request.data
    serializer = TeacherSerializer(data=request_data , many=False)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message': 'Teacher added successfully'})
 except Exception as e:
        return Response(e)
 
@api_view(['GET'])
def getStudent(request):
 try:
    students = Student.objects.all()
    
    serializer_data = StudentSerializer(students, many=True)
#     if serializer_data.is_valid(raise_exception=True):
    return Response(serializer_data.data)
 except Exception as e:
       return Response({"err": e})
 
@api_view(['GET'])
def getTeacher(request):
 try:
    teacher = Teacher.objects.all()
    
    serializer_data = TeacherSerializer(teacher, many=True)
#     f serializer_data.is_valid(raise_exception=True):  
    return Response(serializer_data.data)
 except Exception as e:
       return Response({"err": str(e)})
@api_view(['GET'])
def editStudentData(request,id):
   student = Student.objects.get(id=id)
   serialized_data= StudentSerializer(student, many=False)
   return Response(serialized_data.data)
      
@api_view(['POST'])
def updateStudentData(request,id):
 try:
    student = Student.objects.get(id=id)
    serialized_data= StudentSerializer(student, data=request.data , many=False, partial=True)
    if serialized_data.is_valid(raise_exception=True):
     serialized_data.save()
    return Response({"message": "Student data updated successfully","data":serialized_data.data})
 except Exception as e:
       return Response({"err": e})
 
@api_view(['GET'])
def editTeacherData(request,id):
   teacher = Teacher.objects.get(id=id)
   serialized_data= TeacherSerializer(teacher, many=False)
   return Response(serialized_data.data)

@api_view(['POST'])
def updateTeacherData(request,id):
 try:
    teacher = Teacher.objects.get(id=id)
    serialized_data= TeacherSerializer(teacher, data=request.data , many=False, partial=True)
    if serialized_data.is_valid(raise_exception=True):
     serialized_data.save()
    return Response({"message": "Teacher data updated successfully","data":serialized_data.data})
 except Exception as e:
       return Response({"err": e})
@api_view(['GET'])
def deleteStudentData(request,id):
   student = Student.objects.get(id=id)
   student.delete()
   return Response({"message":"Student data deleted."})
@api_view(['GET'])
def deleteTeacherData(request,id):
   teacher = Teacher.objects.get(id=id)
   teacher.delete()
   return Response({"message":"Teacher data deleted."})

    
