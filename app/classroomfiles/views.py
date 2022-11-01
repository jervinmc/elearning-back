from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import ClassRoomFiles
from .serializers import ClassRoomFilesSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class ClassRoomFilesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=ClassRoomFiles.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=ClassRoomFilesSerializer


class GetFileByProfID(generics.GenericAPIView):
    def get(self,request,format=None,folder_id=None):
        items = ClassRoomFiles.objects.filter(folder_id=folder_id)
        items = ClassRoomFilesSerializer(items,many=True)
        return Response(data = items.data)


