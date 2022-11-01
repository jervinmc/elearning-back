from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Classes
from .serializers import ClassesSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class ClassesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Classes.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=ClassesSerializer


class AdminViewClasses(generics.GenericAPIView):
    def get(self,request,format=None,email=None):
        items = Classes.objects.filter(prof_id=self.request.user.id)
        items = ClassesSerializer(items,many=True)
        return Response(data=items.data)

class AdminViewClasses(generics.GenericAPIView):
    def get(self,request,format=None,email=None):
        items = Classes.objects.filter(prof_id=self.request.user.id)
        items = ClassesSerializer(items,many=True)
        return Response(data=items.data)

