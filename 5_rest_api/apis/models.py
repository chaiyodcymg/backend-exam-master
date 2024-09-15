from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    name_shortness = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Classroom(models.Model):
    grade = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_classrooms')


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    classrooms = models.ManyToManyField(Classroom, related_name='teacher_classrooms')
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
    )
    

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
    )