from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class NeighborhoodList(APIView):
  def get(self,request,format=None):
    neighborhood= Neighborhood.objects.all()
    serializers=NeighborhoodSerializer(neighborhood, many=True)
    return Response(serializers.data)

class BusinessList(APIView):
  def get(self, request,format=None):
    business=Business.objects.all()
    serializers=BusinessSerializers(business, many=True)
    return Response(serializers.data)

class UserList(APIView):
  def get(self,request,format=None):
    users=User.objects.all()
    serializers=UserSerializer(users, many=True)
    return Response(serializers.data)