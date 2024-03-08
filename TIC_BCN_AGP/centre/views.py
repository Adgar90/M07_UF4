from django.shortcuts import render
# Index view

def index(request):
    return render(request, 'index.html')

def students(request):
    return render(request, 'students.html')

def teachers(request):
    return render(request, 'teachers.html')
