from rest_framework import viewsets
from apis.models import School, Classroom , Teacher , Student
from apis.serializers import SchoolSerializer, ClassroomSerializer
from apis.filters import SchoolFilter, ClassroomFilter
from django.db.models import Prefetch
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter