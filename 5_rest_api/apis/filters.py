import django_filters
from .models import School, Classroom, Teacher, Student

class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='school_id')
    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name='classrooms__school__id')
    classroom_id = django_filters.NumberFilter(field_name='classrooms__id')  
    class Meta:
        model = Teacher
        fields = [ 'school_id', 'classroom_id', 'firstname', 'lastname', 'gender']

class StudentFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name='classroom__school__id')
    classroom_id = django_filters.NumberFilter(field_name='classroom__id')  
    class Meta:
        model = Student
        fields = [ 'school_id', 'classroom_id', 'firstname', 'lastname', 'gender']

