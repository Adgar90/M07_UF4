from django.shortcuts import render
from .forms import UserForm
# Funció que mostra el nostre index per defecte
def index(request):
    return render(request, 'index.html')
# Funció que mostra la view de 'students' i que rep com a 'context' els estudiants del centre
def students(request):
    students = [
        {
            'id': 1,
            'nom': 'Adria',
            'cognom1': 'Garcia',
            'cognom2': 'Perez',
            'email': 'adria.garcia@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 2,
            'nom': 'Joana Jiayun',
            'cognom1': 'Lin',
            'cognom2': 'Chen',
            'email': 'joana.lin@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 3,
            'nom': 'Oscar',
            'cognom1': 'Perez',
            'cognom2': 'Mengual',
            'email': 'oscar.perez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 4,
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vazquez',
            'email': 'eric.sanchez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 5,
            'nom': 'Junhong',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'email': 'junhong.zhu@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 6,
            'nom': 'Alexander',
            'cognom1': 'Andreev',
            'cognom2': 'Apukhtina',
            'email': 'alexander.andreev@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 7,
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'email': 'anxo.aragundi@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 8,
            'nom': 'Carlos Andres',
            'cognom1': 'Zambrano',
            'cognom2': 'Aray',
            'email': 'andres.zambrano@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 9,
            'nom': 'Facundo',
            'cognom1': 'Calixto',
            'cognom2': 'Barrios',
            'email': 'facundo.barrios@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 10,
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'email': 'joel.ghanem@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 11,
            'nom': 'Angelo',
            'cognom1': 'Montenegro',
            'cognom2': 'Zavala',
            'email': 'angelo.montenegro@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 12,
            'nom': 'Oriana Saray',
            'cognom1': 'Rojas',
            'cognom2': 'Guedez',
            'email': 'oriana.rojas@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 13,
            'nom': 'Neus',
            'cognom1': 'Bravo',
            'cognom2': 'Arias',
            'email': 'neus.bravo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 14,
            'nom': 'Angel',
            'cognom1': 'Ivanov',
            'cognom2': 'Spasov',
            'email': 'angel.ivanov@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 15,
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': 'Kha',
            'email': 'dinar.kha@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 16,
            'nom': 'Jesus',
            'cognom1': 'Pujada',
            'cognom2': 'Montoya',
            'email': 'jesus.pujada@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 17,
            'nom': 'Veronica',
            'cognom1': 'Cartagena',
            'cognom2': 'Jaldin',
            'email': 'veronica.cartagena@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 18,
            'nom': 'Gemma',
            'cognom1': 'Garrigosa',
            'cognom2': 'Frances',
            'email': 'gemma.garrigosa@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        }
    ]
    context = { 'students': students }
    return render(request, 'students.html', context)
# Funció que mostra la view de 'teachers' i que rep com a 'context' els professors del centre
def teachers(request):
    teachers = [
    {
        'id':1,
        'nom': 'Juanma',
        'cognom1': 'Sanchez',
        'cognom2': 'Bel',
        'email': 'juanmanuel.sanchez@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': True,
        'modul': 'M06'
    },
    {
        'id':2,
        'nom': 'Roger',
        'cognom1': 'Sobrino',
        'cognom2': 'Gil',
        'email': 'roger.sobrino@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': False,
        'modul': 'M07'
    },
    {
        'id':3,
        'nom': 'Josep Oriol',
        'cognom1': 'Roca',
        'cognom2': 'Fabra',
        'email': 'joseporiol.roca@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': False,
        'modul': 'M09'
    },
    {
        'id':4,
        'nom': 'Xavi',
        'cognom1': 'Quesada',
        'cognom2': 'Puertas',
        'email': 'xavi.quesada@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': False,
        'modul': 'M08, MAH'
    }
]
    context = { 'teachers': teachers }
    return render(request, 'teachers.html', context)
# Funció que mostra la informació completa d'un estudiant en concret i que rep la seva id com a paràmetre
def student(request, id):
    students = [
        {
            'id': 1,
            'nom': 'Adria',
            'cognom1': 'Garcia',
            'cognom2': 'Perez',
            'email': 'adria.garcia@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 2,
            'nom': 'Joana Jiayun',
            'cognom1': 'Lin',
            'cognom2': 'Chen',
            'email': 'joana.lin@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 3,
            'nom': 'Oscar',
            'cognom1': 'Perez',
            'cognom2': 'Mengual',
            'email': 'oscar.perez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 4,
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vazquez',
            'email': 'eric.sanchez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 5,
            'nom': 'Junhong',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'email': 'junhong.zhu@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 6,
            'nom': 'Alexander',
            'cognom1': 'Andreev',
            'cognom2': 'Apukhtina',
            'email': 'alexander.andreev@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 7,
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'email': 'anxo.aragundi@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 8,
            'nom': 'Carlos Andres',
            'cognom1': 'Zambrano',
            'cognom2': 'Aray',
            'email': 'andres.zambrano@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 9,
            'nom': 'Facundo',
            'cognom1': 'Calixto',
            'cognom2': 'Barrios',
            'email': 'facundo.barrios@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 10,
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'email': 'joel.ghanem@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 11,
            'nom': 'Angelo',
            'cognom1': 'Montenegro',
            'cognom2': 'Zavala',
            'email': 'angelo.montenegro@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 12,
            'nom': 'Oriana Saray',
            'cognom1': 'Rojas',
            'cognom2': 'Guedez',
            'email': 'oriana.rojas@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 13,
            'nom': 'Neus',
            'cognom1': 'Bravo',
            'cognom2': 'Arias',
            'email': 'neus.bravo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 14,
            'nom': 'Angel',
            'cognom1': 'Ivanov',
            'cognom2': 'Spasov',
            'email': 'angel.ivanov@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 15,
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': 'Kha',
            'email': 'dinar.kha@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 16,
            'nom': 'Jesus',
            'cognom1': 'Pujada',
            'cognom2': 'Montoya',
            'email': 'jesus.pujada@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 17,
            'nom': 'Veronica',
            'cognom1': 'Cartagena',
            'cognom2': 'Jaldin',
            'email': 'veronica.cartagena@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        },
        {
            'id': 18,
            'nom': 'Gemma',
            'cognom1': 'Garrigosa',
            'cognom2': 'Frances',
            'email': 'gemma.garrigosa@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09'
        }
    ]
    student_obj = None
    for i in students:
        if (i['id'] == id):
            student_obj = i
    return render(request, 'student.html', {'student':student_obj})
# Funció que mostra la informació completa d'un professor en concret i que rep la seva id com a paràmetre
def teacher(request, id):
    teachers = [
    {
        'id':1,
        'nom': 'Juanma',
        'cognom1': 'Sanchez',
        'cognom2': 'Bel',
        'email': 'juanmanuel.sanchez@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': True,
        'modul': 'M06'
    },
    {
        'id':2,
        'nom': 'Roger',
        'cognom1': 'Sobrino',
        'cognom2': 'Gil',
        'email': 'roger.sobrino@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': False,
        'modul': 'M07'
    },
    {
        'id':3,
        'nom': 'Josep Oriol',
        'cognom1': 'Roca',
        'cognom2': 'Fabra',
        'email': 'joseporiol.roca@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': False,
        'modul': 'M09'
    },
    {
        'id':4,
        'nom': 'Xavi',
        'cognom1': 'Quesada',
        'cognom2': 'Puertas',
        'email': 'xavi.quesada@iticbcn.cat',
        'curs': 'DAM2A, DAW2B',
        'tutor': False,
        'modul': 'M08, MAH'
    }
]
    teacher_obj = None
    for i in teachers:
        if (i['id'] == id):
            teacher_obj = i
    return render(request, 'teacher.html', {'teacher':teacher_obj})
# Funció que crea un formulari i el redirigeix com a context a la view d'user_form
def user_form(request):
    form = UserForm()
    context = {"form":form}
    return render(request, 'user_form.html', context)
