from rest_framework import serializers
from .models import LocalFiles

class LocalFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=LocalFiles
        fields="__all__"
