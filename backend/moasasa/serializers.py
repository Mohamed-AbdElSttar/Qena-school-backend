from rest_framework import serializers
from .models import Student, Teacher, CoursesGroup, Post, Admin, Membership


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CoursesGroupSerializer(serializers.ModelSerializer):
    teacher_pk = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True
    )

    class Meta:
        model = CoursesGroup
        fields = ['id', 'name', 'level', 'session_num',
                  'start_date', 'schedule', 'teacher_pk', 'teacher']
        depth = 1


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
