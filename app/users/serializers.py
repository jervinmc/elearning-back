from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password, ValidationError
from django.contrib.auth.models import Group, Permission

class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    class Meta:
        
        model=User
        # fields="__all__"
        exclude = ['last_login',
                   'is_staff', 'user_permissions']
    
    def validate_password(self, value):
        try:
            validate_password(value, self)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        
        email = validated_data.pop('email')
        # password = validated_data.pop('password')
        password = validated_data.pop('password')
        # groups = validated_data.pop('groups')
        
        user = User.objects.create_user(
            email=email, password=password, **validated_data)
        # for g in groups:
        #     user.groups.add(g.id)
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

class GetUserSerializer(serializers.ModelSerializer):

    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)
        depth = 1
        
class GetUserSerializerExcludePassword(serializers.ModelSerializer):
    class Meta:
        model=User
        # fields="__all__"
        exclude=('password',)