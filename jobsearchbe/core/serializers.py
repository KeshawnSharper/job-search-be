from rest_framework import serializers
from .models import User
from django import forms
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id','password','email','username'
        ]

# class RegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style = {'input_type' : 'password'},write_only = True)
#     class Meta:
#         model = User
#         fields = [
#             'id','password','email','username','password2'
#         ]
#         extra_kwargs = {
# 				'password': {'write_only': True},
# 		}	
#     def	save(self):
#         account = {}
#         (
#         email=self.validated_data['email'],
#         username=self.validated_data['username']
#         )
#         account.email = Userself.validated_data['email'])
#         account.email
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         account.set_password(password)
#         account.save()
#         return account
