from rest_framework import serializers
from .models import ClassRoomFolder

class ClassRoomFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassRoomFolder
        fields="__all__"
