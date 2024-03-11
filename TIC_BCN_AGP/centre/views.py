from django.shortcuts import render
# Index view

def index(request):
    return render(request, 'index.html')

def students(request):
    students = [
        {
            'nom':'Adria',
            'cognom1':'Garcia',
            'cognom2':'Perez',
            'email':'adria.garcia@iticbcn.cat',
            'curs':'DAW2A',
            'moduls': ['M06', 'M07', 'M08', 'M09']
        }
    ]
    context = { 'students': students }
    return render(request, 'students.html', context)

def teachers(request):
    teachers = [
        {
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'email': 'juanmanuel.sanchez@iticbcn.cat',
            'curs': ['DAM2B', 'DAW2A'],
            'tutor': True,
            'modul': 'M06'
        },
        {
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'email': 'roger.sobrino@iticbcn.cat',
            'curs': ['DAM2B', 'DAW2A'],
            'tutor': False,
            'modul': 'M07'
        },
        {
            'nom': 'Josep Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'email': 'joseporiol.rpca@iticbcn.cat',
            'curs': ['DAM2B', 'DAW2A'],
            'tutor': False,
            'modul': 'M09'
        }
    ]
    context = teachers
    return render(request, 'teachers.html', context)
