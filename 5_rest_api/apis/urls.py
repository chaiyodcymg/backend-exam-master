from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolViewSet , ClassroomViewSet
from apis.views.v1.student import StudentViewSet
from apis.views.v1.teacher import TeacherViewSet

router = DefaultRouter()
router.register(r'school', SchoolViewSet)
router.register(r'classroom', ClassroomViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
