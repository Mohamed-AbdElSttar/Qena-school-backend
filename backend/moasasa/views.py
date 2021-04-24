from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MembershipSerializer, PostSerializer, CoursesGroupSerializer, StudentSerializer

from .models import *
# Create your views here.


@api_view(['GET'])
def get_post_group(request, id):
    queryset = Post.objects.filter(group=id)
    if request.method == 'GET':
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_teacher_groups(request, id):
    queryset = CoursesGroup.objects.filter(teacher=id)
    if request.method == 'GET':
        serializer = CoursesGroupSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_student_mempership(request, id):
    queryset = Membership.objects.filter(student=id)
    if request.method == 'GET':
        serializer = MembershipSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_student_by_user_id(request,user_id):
    print("new api works",user_id)
    queryset=Student.objects.filter(user=user_id).first()
    print(queryset)
    if queryset:
        serializer=StudentSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({
            "message":status.HTTP_404_NOT_FOUND
        })



@api_view(['POST'])
def groups_search(request):
    name = request.data.get('name')
    level = request.data.get('level')
    if name == "":
        queryset = CoursesGroup.objects.filter(level=level)
    elif level == "":
        queryset = CoursesGroup.objects.filter(name=name,)
    else:
        queryset = CoursesGroup.objects.filter(name=name, level=level)

    if request.method == 'POST':
        serializer = CoursesGroupSerializer(queryset, many=True)
        return Response(serializer.data)
