from django.contrib import admin
from django.urls import path
from  .views import *
urlpatterns = [
    # add data
    path('add-student/',postStudent), 
    path('add-teacher/',postTeacher),
    # get data
    path('get-student/',getStudent),
    path('get-teacher/',getTeacher),
    # edit data
    path('edit-student/<int:id>/',editStudentData),
    path('update-student/<int:id>/',updateStudentData),
    path('edit-teacher/<int:id>/',editTeacherData),
    path('update-teacher/<int:id>/',updateTeacherData),
    
    #delete data
    path('delete-student/<int:id>/',deleteStudentData),
    path('delete-teacher/<int:id>/',deleteTeacherData),
]


    
