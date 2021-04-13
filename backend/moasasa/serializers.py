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

    class Meta:
        model = CoursesGroup
        fields = '__all__'
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'