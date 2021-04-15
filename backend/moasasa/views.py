from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer

from .models import *
# Create your views here.
@api_view(['GET'])
def get_post_group(request,id):
    print("yes it works works")
    queryset=Post.objects.filter(group=id)
    if request.method == 'GET':
        serializer = PostSerializer(queryset,many=True)
        return Response(serializer.data)
