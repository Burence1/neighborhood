from django.db import models
from django.db.models import fields
from .models import Profile, User,Neighborhood,Business,Post
from rest_framework import serializers
from django import forms


class BusinessSerializers(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  class Meta:
    model = User
    fields = ['username','email','password']


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
  # user=UserSerializer(read_only=True,many=False)
  business = BusinessSerializers(many=True, read_only=True)

  class Meta:
    model = Profile
    fields="__all__"


class NeighborhoodSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(many=True, read_only=True)
  business = BusinessSerializers(many=True, read_only=True)

  class Meta:
    model = Neighborhood
    fields = '__all__'


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "password"]