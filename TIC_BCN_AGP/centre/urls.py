from django.urls import path
from . import views
urlpatterns = [
    #Path a index per defecte
    path('', views.index, name='index'),
    #Path (/students/) que crida la funció students de views.py
    path('students', views.students, name='students'),
    #Path (/teachers/) que crida la funció teachers de views.py
    path('teachers', views.teachers, name='teachers'),
    #Path (/students/student/1) que crida la funció student de views.py i la qual rep la id com a paràmetre
    path('students/student/<int:id>', views.student, name='student'),
    #Path (/teachers/teacher/1) que crida la funció teacher de views.py i la qual rep la id com a paràmetre
    path('teachers/teacher/<int:id>', views.teacher, name='teacher'),
]