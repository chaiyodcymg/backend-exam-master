from rest_framework import viewsets
from apis.models import Student
from apis.serializers import StudentSerializer
from apis.filters import StudentFilter
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter