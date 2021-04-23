from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt,datetime
from rest_framework.views import APIView

# Create your views here.

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed('User Not Found')
    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password')
    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow()
    }

    token = jwt.encode(
        payload, 'django-insecure-45-%2klm@4jhgrqi=_wvs8bc1us97kke_1r(pm*o+70t4c(*_6', algorithm='HS256')
    response = Response()
    response.set_cookie('jwt_cookie', token, httponly=True)
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
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt_cookie')
        print('token : ', token)
        print('token type : ', type(token))

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(
                token, 'django-insecure-45-%2klm@4jhgrqi=_wvs8bc1us97kke_1r(pm*o+70t4c(*_6', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('User Not Authenticated')
        user = User.objects.filter(id=payload['id']).first()
        serilaizer = UserSerializer(user)
        return Response(serilaizer.data)
    

