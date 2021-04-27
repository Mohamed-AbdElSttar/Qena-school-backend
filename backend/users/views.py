from re import A
from django.db.models import manager
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt
import datetime
from rest_framework.views import APIView
from django.core.mail import send_mail
import uuid
from django.contrib.auth.hashers import make_password
from moasasa.serializers import StudentSerializer, TeacherSerializer, AdminSerializer

code=''
EMAIL=''
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed('User Not Found')
    if not user.check_password(password):
        print(password)
        raise AuthenticationFailed('Incorrect password')
    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow()
    }

    token = jwt.encode(
        payload, 'django-insecure-45-%2klm@4jhgrqi=_wvs8bc1us97kke_1r(pm*o+70t4c(*_6', algorithm='HS256')
    response = Response()
    response.set_cookie('jwt_cookie', token, httponly=True, samesite='lax')
    response.data = {
        'jwt_token': token
    }

    return response


@api_view(['POST'])
def logout_user(request):
    response = Response()
    response.delete_cookie('jwt_cookie')
    response.data = {
        'message': status.HTTP_200_OK
    }
    return response


class RegisterView(APIView):
    def post(self, request):
        print("Request data : ", request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def post(self, request):
        token = request.data.get('jwt_token')

        if not token:
            raise AuthenticationFailed('un Authenticated user')
        try:
            print("in try")
            print(token)
            payload = jwt.decode(
                token, 'django-insecure-45-%2klm@4jhgrqi=_wvs8bc1us97kke_1r(pm*o+70t4c(*_6', algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('User Not Authenticated')
        user = User.objects.filter(id=payload['id']).first()
        serilaizer = UserSerializer(user)
        return Response(serilaizer.data)


@api_view(['POST'])
def register_student(request):
    email = request.data.get('email')
    password = request.data.get('password')
    password1 = request.data.get('password1')
    if not password == password1:
        raise AuthenticationFailed('2 Passwords is not identcal ')
    name = request.data.get('name')
    level = request.data.get('level')
    phone = request.data.get('phone')
    image = request.data.get('image')
    requestUser = {
        'email': email,
        'password': password,
        'role': 'student'
    }

    user = User.objects.filter(email=email).first()
    if user:
        raise AuthenticationFailed('User Already Exist')
    userSerializer = UserSerializer(data=requestUser)
    userSerializer.is_valid(raise_exception=True)
    userSerializer.save()

    user = User.objects.filter(email=email).first()

    requestStudent = {
        'user': user.id,
        'name': name,
        'level': level,
        'phone': phone,
        'image': image
    }
    studentSerializer = StudentSerializer(data=requestStudent)
    studentSerializer.is_valid(raise_exception=True)
    studentSerializer.save()

    return Response({'user': userSerializer.data, 'student': studentSerializer.data}, status.HTTP_200_OK)


@api_view(['POST'])
def register_teacher(request):
    email = request.data.get('email')
    password = request.data.get('password')
    password1 = request.data.get('password1')
    if not password == password1:
        raise AuthenticationFailed('2 Passwords is not identcal ')
    name = request.data.get('name')
    description = request.data.get('description')
    phone = request.data.get('phone')
    image = request.data.get('image')
    requestUser = {
        'email': email,
        'password': password,
        'role': 'teacher'
    }

    user = User.objects.filter(email=email).first()
    if user:
        raise AuthenticationFailed('User Already Exist')
    userSerializer = UserSerializer(data=requestUser)
    userSerializer.is_valid(raise_exception=True)
    userSerializer.save()

    user = User.objects.filter(email=email).first()

    requestTeacher = {
        'user': user.id,
        'name': name,
        'description': description,
        'phone': phone,
        'image': image
    }
    teacherSerializer = TeacherSerializer(data=requestTeacher)
    teacherSerializer.is_valid(raise_exception=True)
    teacherSerializer.save()

    return Response({'user': userSerializer.data, 'student': teacherSerializer.data}, status.HTTP_200_OK)


@api_view(['POST'])
def register_admin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    password1 = request.data.get('password1')
    if not password == password1:
        raise AuthenticationFailed('2 Passwords is not identcal ')
    name = request.data.get('name')
    manager = request.data.get('manager')
    ssn = request.data.get('ssn')
    requestUser = {
        'email': email,
        'password': password,
        'role': 'admin'
    }

    user = User.objects.filter(email=email).first()
    if user:
        raise AuthenticationFailed('هذا المستخدم موجود بالفعل')
    userSerializer = UserSerializer(data=requestUser)
    userSerializer.is_valid(raise_exception=True)
    userSerializer.save()

    user = User.objects.filter(email=email).first()

    requestAdmin = {
        'user': user.id,
        'name': name,
        'manager': manager,
        'ssn': ssn
    }
    adminSerializer = AdminSerializer(data=requestAdmin)
    adminSerializer.is_valid(raise_exception=True)
    adminSerializer.save()

    return Response({'user': userSerializer.data, 'admin': adminSerializer.data}, status.HTTP_200_OK)

@api_view(['POST'])
def check_mail(request):
    user=User.objects.filter(email=request.data.get('email')).first()
    if user:
        serializer=UserSerializer(user)
        return Response(serializer.data)
    raise AuthenticationFailed('هذا البريد الاليكتروني غير موجود')

@api_view(['POST'])
def generate_code_reset_password(request):
    email=request.data.get('email')
    global EMAIL
    global code
    EMAIL=email
    code= uuid.uuid4().hex.upper()[0:6]
    subject="رمز اعادة تعيين كلمة المرور من موقع الخدمات الالكترونية"
    send_mail(
        subject,
        code,
        'testerdjango6@gmail.com',
        [email,],
        fail_silently=False,
    )
    return Response({
        'code':code
    })

@api_view(['POST'])
def check_code_validity(request):
    print(code)
    print(EMAIL,"email ")
    if request.data.get('code')==code:
        return Response({
            'status':status.HTTP_200_OK
        })
    else:
        raise AuthenticationFailed('برجاء ادخل الكود الصحيح')

@api_view(['PUT'])
def reset_password(request):
    password1=request.data.get('password1')
    password2= request.data.get('password2')
    if password1==password2:
        user=User.objects.filter(email=EMAIL).first()
        password1=make_password(password1)
        updated_data={
        'email': EMAIL,
        'password': password1,
        'role': user.role
                    }
        serializer=UserSerializer(user,data=updated_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':status.HTTP_202_ACCEPTED
            })
        raise AuthenticationFailed('not changed')
    raise AuthenticationFailed('كلمات المرور غير متطابقة')




