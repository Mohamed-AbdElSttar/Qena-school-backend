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
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        print("POST works")
        print(request.data)
        name = request.data['name']
        print("hhhhhhhhhhhhhhh",request.data['description'])
        description = request.data['description']
        phone = request.data['phone']
        image = request.data['image']
        print( "oooooooooooooo")
        Teacher.objects.create(name=name, description=description, phone=phone, image=image)
        return HttpResponse({"created": "created"}, status=200)
    def update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        print("update works")
        print(request.data)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse({"updated": "updated"}, status=200)

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