from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser

from .serializers import *
from rest_framework import viewsets
from .models import *


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacheViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseGroupViewset(viewsets.ModelViewSet):
    queryset = CoursesGroup.objects.all()
    serializer_class = CoursesGroupSerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AdminViewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class MembershipViewset(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
