from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
# Funció que mostra el nostre index per defecte
def index(request):
    return render(request, 'index.html')
# Funció que mostra la view de 'students' i que rep com a 'context' els estudiants del centre
def students(request):
    students = User.objects.filter(role="S")
    print(students)
    context = { 'students': students }
    return render(request, 'students.html', context)
# Funció que mostra la view de 'teachers' i que rep com a 'context' els professors del centre
def teachers(request):
    teachers = User.objects.filter(role="T")
    context = { 'teachers': teachers }
    return render(request, 'teachers.html', context)
# Funció que mostra la informació completa d'un estudiant en concret i que rep la seva id com a paràmetre
def student(request, id):
    student = User.objects.get(id=id)
    return render(request, 'student.html', {'student':student})
# Funció que mostra la informació completa d'un professor en concret i que rep la seva id com a paràmetre
def teacher(request, id):
    teacher = User.objects.get(id=id)
    return render(request, 'teacher.html', {'teacher':teacher})
# Funció que crea un formulari i el redirigeix com a context a la view d'user_form
def user_form(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            role_template = 'students' if form['role'].value() == "S" else 'teachers'
            return redirect(role_template)
    context = {"form":form}
    return render(request, 'user_form.html', context)

