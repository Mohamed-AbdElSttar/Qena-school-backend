from django.db import models
from users.models import User
import datetime
from django.core.validators import RegexValidator

STATUS_TYPE = (
    ("binding", "binding"),
    ("active", "active"),
)

LEVELS = (
    ("اول ابتدائي", "اول ابتدائي"),
    ("ثاني ابتدائي", "ثاني ابتدائي"),
    ("ثالث ابتدائي", "ثالث ابتدائي"),
    ("رابع ابتدائي", "رابع ابتدائي"),
    ("خامس ابتدائي", "خامس ابتدائي"),
    ("سادس ابتدائي", "سادس ابتدائي"),
    ("اول اعدادي", "اول اعدادي"),
    ("ثاني اعدادي", "ثاني اعدادي"),
    ("ثالث اعدادي", "ثالث اعدادي"),
    ("اول ثانوي", "اول ثانوي"),
    ("ثاني ثانوي", "ثاني ثانوي"),
    ("ثالث ثانوي", "ثالث ثانوي"),
    ("اخري", "اخري"),
)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    level = models.CharField(choices=LEVELS, max_length=20)
    phone = models.CharField(max_length=11)
    image = models.ImageField(
        upload_to="moasasa/students/images",
        default="moasasa/students/images/default.jpg",
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    image = models.ImageField(
        upload_to="moasasa/teachers/images",
        default="moasasa/teachers/images/default.jpg",
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class CoursesGroup(models.Model):
    name = models.CharField(max_length=50, null=False)
    level = models.CharField(choices=LEVELS, max_length=55)
    teacher = models.ForeignKey(
        Teacher,
        related_name="coursesGroup_teacher",
        null=False,
        on_delete=models.CASCADE,
    )
    session_num = models.IntegerField(null=False)
    start_date = models.DateField(null=False)
    next_session_date = models.DateField(null=False)
    next_session_time = models.TimeField(null=False)
    schedule = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    capacity = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    group = models.ForeignKey(
        CoursesGroup,
        related_name="coursesGroup_post",
        null=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group.name


class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    manager = models.ForeignKey(
        "self", null=True, related_name="admin", on_delete=models.SET_NULL
    )
    ssn = models.CharField(null=False, validators=[RegexValidator(
        regex='^[0-9]{14}$', message='Length has to be 14', code='nomatch')], max_length=14, unique=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(
        CoursesGroup, related_name="membership", on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        Student, related_name="membership", on_delete=models.CASCADE
    )

    status = models.CharField(choices=STATUS_TYPE, max_length=20)
    image = models.ImageField(
        upload_to="moasasa/reservation/images",
        default="moasasa/reservation/images/default.jpg",
        blank=True, null=True
    )

    def __str__(self):
        return "{} in {}".format(self.student.name, self.group.name)
