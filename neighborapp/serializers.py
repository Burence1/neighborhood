from django.db import models
from django.db.models import fields
from .models import User,Neighborhood,Business
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['neighborhood']

class NeighborhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Neighborhood
    fields=["name","location"]

class BusinessSerializers(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields=["name","email"]