from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt,datetime
# Create your views here.

@api_view(['POST'])
def login_user(request):
    email=request.data.get('email')
    password=request.data.get('password')
    user=User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed('User Not Found')
    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password')
    payload={
        'id':user.id,
        'exp':datetime.datetime.now().minute+60,
        'iat':datetime.datetime.now()
    }

    token=jwt.encode(payload,'django-insecure-45-%2klm@4jhgrqi=_wvs8bc1us97kke_1r(pm*o+70t4c(*_6',algorithm='HS256')
    response=Response()
    response.set_cookie('jwt_cookie',token,httponly=True)
    response.data={
        'jwt_token':token
    }

    return response


@api_view(['POST'])
def logout_user(request):
    response=Response()
    response.delete_cookie('jwt_cookie')
    response.data={
        'message':status.HTTP_200_OK
    }
    return response