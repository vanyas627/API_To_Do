from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from datetime import date

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_title(self,value):
        if len(value) < 3:
            raise serializers.ValidationError('Title must have more than 3 symbols')
        return value



class SerializerRegister(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


