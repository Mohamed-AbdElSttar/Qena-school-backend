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
    group_pk = serializers.PrimaryKeyRelatedField(
        queryset=CoursesGroup.objects.all(), source='group', write_only=True
    )

    class Meta:
        model = Post
        fields = ['group', 'title', 'content', 'created_at', 'group_pk']
        depth = 1


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    group_pk = serializers.PrimaryKeyRelatedField(
        queryset=CoursesGroup.objects.all(), source='group', write_only=True
    )
    student_pk = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True)

    class Meta:
        model = Membership
        fields = ['id', 'group', 'student', 'student_pk',
                  'status', 'validation_code', 'group_pk']
        depth = 2
