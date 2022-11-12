from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Enrolled
from .serializers import EnrolledSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from classes.models import Classes
from classes.serializers import ClassesSerializer
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class EnrolledView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Enrolled.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=EnrolledSerializer
    
    def create(self,request,format=None):
        res = request.data
        item = EnrolledSerializer(data=res)
        item.is_valid(raise_exception=True)
        item.save()
        return Response(data=item.data)
        


class viewByStudent(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        items = Enrolled.objects.filter(student_id = self.request.user.id,status='Not Archived')
        items = EnrolledSerializer(items, many=True)
        for x in items.data:
            classes = Classes.objects.filter(code=x['code'])
            classes = ClassesSerializer(classes,many=True)
            if(len(classes.data)!=0):
                x['class_name'] = classes.data[0]['class_name']
        return Response(status=status.HTTP_200_OK,data=items.data)

class viewByStudentArchived(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        items = Enrolled.objects.filter(student_id = self.request.user.id,status='Archived')
        items = EnrolledSerializer(items, many=True)
        for x in items.data:
            classes = Classes.objects.filter(code=x['code'])
            classes = ClassesSerializer(classes,many=True)
            if(len(classes.data)!=0):
                x['class_name'] = classes.data[0]['class_name']
        return Response(status=status.HTTP_200_OK,data=items.data)

class viewByCode(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request,code=None):
        items = Enrolled.objects.filter(code=code,status='Not Archived')
        items = EnrolledSerializer(items, many=True)
        for x in items.data:
            user = User.objects.filter(id=x['student_id'])
            user = GetUserSerializer(user,many=True)
            x['name'] = f"{user.data[0]['firstname']} {user.data[0]['lastname']}"
        return Response(status=status.HTTP_200_OK,data=items.data)