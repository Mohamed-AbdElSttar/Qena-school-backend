from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from .serializers import MembershipSerializer, PostSerializer, CoursesGroupSerializer, StudentSerializer, TeacherSerializer, AdminSerializer

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
def get_student_by_user_id(request, user_id):
    queryset = Student.objects.filter(user=user_id).first()
    if queryset:
        serializer = StudentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({
            "message": status.HTTP_404_NOT_FOUND
        })


@api_view(["GET"])
def get_teacher_by_user_id(request, id):
    queryset = Teacher.objects.filter(user=id).first()
    if queryset:
        serializer = TeacherSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({
        'message': status.HTTP_404_NOT_FOUND
    })


@api_view(['GET'])
def get_admin_by_user_id(request, user_id):
    queryset = Admin.objects.filter(user=user_id).first()
    if queryset:
        serializer = AdminSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({
        'message': status.HTTP_404_NOT_FOUND
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

@api_view(['GET'])
def today_groups(request):
    groups=CoursesGroup.objects.filter(next_session_date=datetime.datetime.today())
    serializer=CoursesGroupSerializer(groups,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def send_meeting_url(request):
    group_id=request.data.get('group_id')
    emails = []
    user_id=request.data.get('user_id')
    teacher_user=User.objects.filter(id=user_id)
    url=request.data.get('url')
    emails.append(teacher_user)
    memberships=Membership.objects.filter(group=group_id)
    for mem in memberships:
        if mem.status=='active':
            student=Student.objects.filter(id=mem.student).first()
            std_user=User.objects.filter(id=student.user)
            emails.append(std_user.email)
    if emails:
        print(emails)
        return Response({
            'message':status.HTTP_200_OK
        })
    else:
        raise AuthenticationFailed('انتهت حجوزات هذه المحموعة')


