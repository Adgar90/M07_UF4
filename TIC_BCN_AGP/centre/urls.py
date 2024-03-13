from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('teachers', views.teachers, name='teachers'),
    path('students/student/<int:id>', views.student, name='student'),
    path('teachers/teacher/<int:id>', views.teacher, name='teacher'),
]