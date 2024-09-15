from rest_framework import serializers
from apis.models import School, Classroom, Teacher, Student
from rest_framework.exceptions import ValidationError
class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'name_shortness', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.school_classrooms.count()
    
    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__in=obj.school_classrooms.all()).distinct().count()
    
    def get_student_count(self, obj):
        return sum(classroom.students.count() for classroom in obj.school_classrooms.all())
    
class ClassroomSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField()
    teachers = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    class Meta:
        model = Classroom
        fields = [ 'id', 'grade', 'section', 'school_id' , 'teachers' ,'students' ]

    def create(self, validated_data):
        school_id = validated_data.pop('school_id')
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            raise ValidationError("School with this ID does not exist.")
        return Classroom.objects.create(school=school, **validated_data)
    
    def update(self, instance, validated_data):
        school_id = validated_data.pop('school_id', None)
        if school_id:
            try:
                instance.school = School.objects.get(id=school_id)
            except School.DoesNotExist:
                raise ValidationError("School with this ID does not exist.")
        return super().update(instance, validated_data)
    
    def get_teachers(self, obj):
        teachers = Teacher.objects.filter(classrooms=obj)
        serializer = TeacherSerializer(teachers, many=True)
        return serializer.data
    
    def get_students(self, obj):
        students = Student.objects.filter(classroom=obj)
        serializer = StudentSerializer(students, many=True)
        return serializer.data

class TeacherSerializer(serializers.ModelSerializer):
    classroom_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender', 'classroom_ids' , 'classrooms']
        read_only_fields = ['classrooms']
    
    def create(self, validated_data):
        classroom_ids = validated_data.pop('classroom_ids', [])
        teacher = super().create(validated_data)
        if classroom_ids:
            classrooms = Classroom.objects.filter(id__in=classroom_ids)
            if not classrooms.exists():
                raise ValidationError("Classroom with this ID does not exist.")
            teacher.classrooms.set(classrooms)
        return teacher
    
    def update(self, instance, validated_data):
        classroom_ids = validated_data.pop('classroom_ids', [])
        teacher = super().update(instance, validated_data)
        if classroom_ids:
            classrooms = Classroom.objects.filter(id__in=classroom_ids)
            if not classrooms.exists():
                raise ValidationError("Classroom with this ID does not exist.")
            teacher.classrooms.set(classrooms)
        return teacher
    
class StudentSerializer(serializers.ModelSerializer):
    classroom_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Student
        fields = ['id', 'firstname', 'lastname', 'gender', 'classroom_id' , 'classroom']
        read_only_fields = ['classroom']

    def create(self, validated_data):
        classroom_id = validated_data.pop('classroom_id')
        try:
            classroom = Classroom.objects.get(id=classroom_id)
        except Classroom.DoesNotExist:
            raise ValidationError("Classroom with this ID does not exist.")
        return Student.objects.create(classroom=classroom, **validated_data)
    
    def update(self, instance, validated_data):
        classroom_id = validated_data.pop('classroom_id', None)
        if classroom_id:
            try:
                instance.classroom = Classroom.objects.get(id=classroom_id)
            except Classroom.DoesNotExist:
                raise ValidationError("Classroom with this ID does not exist.")
        return super().update(instance, validated_data)