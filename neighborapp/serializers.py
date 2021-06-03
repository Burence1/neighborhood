from django.db import models
from django.db.models import fields
from .models import User,Neighborhood,Business
from rest_framework import serializers


class BusinessSerializers(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = "__all__"

    # def create(self,validated_data):
    #   business=Business.objects.create(
    #     name=validated_data['name'],
    #     email=validated_data['email'],
    #     neighborhood=validated_data['neighborhood'],
    #     user=validated_data['user']
    #   )
    #   business.save()
    #   return business

class UserSerializer(serializers.ModelSerializer):
  business=BusinessSerializers(many=True,read_only=True)
  class Meta:
    model = User
    fields = "__all__"

    # def create(self,validated_data):
    #   user=User.objects.create(
    #     name=validated_data['name'],
    #     email=validated_data['email'],
    #     business=validated_data['business']
    #   )
    #   user.save()
    #   return user

class NeighborhoodSerializer(serializers.ModelSerializer):
  users=UserSerializer(many=True,read_only=True)
  business=BusinessSerializers(many=True,read_only=True)
  class Meta:
    model = Neighborhood
    fields="__all__"

    # def create(self,validate_data):
    #   neighbor=Neighborhood.objects.create(
    #     name=validate_data['name'],
    #     location=validate_data['location'],
    #     users=validate_data['users'],
    #     business=validate_data['business'],
    #   )

    #   neighbor.save()
    #   return neighbor