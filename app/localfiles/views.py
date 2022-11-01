from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import LocalFiles
from .serializers import LocalFilesSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class LocalFilesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=LocalFiles.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=LocalFilesSerializer

    def list(self,request,format=None):
        items = LocalFiles.objects.filter(user_id = self.request.user.id)
        items = LocalFilesSerializer(items,many=True)
        return Response(data= items.data)


