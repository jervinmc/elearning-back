from rest_framework import serializers
from .models import ClassRoomFiles

class ClassRoomFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassRoomFiles
        fields="__all__"
