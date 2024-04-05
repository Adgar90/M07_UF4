from django.db import models

# Create your models here.
class User(models.Model):
    ROLES = [
        ("S", "Student"),
        ("T", "Teacher")
    ]
    nom = models.CharField(max_length=30)
    cognom1 = models.CharField(max_length=30)
    cognom2 = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    curs = models.CharField(max_length=30)
    moduls = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=ROLES)