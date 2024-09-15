from rest_framework import viewsets
from apis.models import Teacher
from apis.serializers import TeacherSerializer
from apis.filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter
