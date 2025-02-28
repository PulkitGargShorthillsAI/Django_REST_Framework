from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.

def studentsView(request):
    students = Student.objects.all()
    students_list = list(students.values())
    print(students_list)
    return JsonResponse(students_list,safe=False)
