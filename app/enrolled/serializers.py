from rest_framework import serializers
from .models import Enrolled

class EnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrolled
        fields="__all__"
