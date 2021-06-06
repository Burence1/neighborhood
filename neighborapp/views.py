from os import stat
from django.core.checks import messages
from django.shortcuts import render
from rest_framework import filters
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404,QueryDict
from django.http import response
from rest_framework import generics
from rest_framework import filters
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.
class NeighborhoodList(APIView):
  serializer_class=NeighborhoodSerializer
  def get_neighborhood(self,pk):
    try:
        return Neighborhood.objects.get(pk=pk)
    except Neighborhood.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    neighborhood= Neighborhood.objects.all()
    serializers=self.serializer_class(neighborhood, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      neighborhood=serializers.data
      response = {
          'data': {
              'neighborhood': dict(neighborhood),
              'status': 'success',
              'message': 'neighborhood created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    serializers = self.serializer_class(neighborhood, request.data)
    if serializers.is_valid():
      serializers.save()
      neighborhood=serializers.data
      response = {
          'data': {
              'neighborhood': dict(neighborhood),
              'status': 'success',
              'message': 'neighborhood updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    neighborhood.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):
  serializer_class=BusinessSerializers
  def get_business(self, pk):
    try:
        return Business.objects.get(pk=pk)
    except Business.DoesNotExist:
        return Http404()

  def get(self, request,format=None):
    business=Business.objects.all()
    serializers=self.serializer_class(business, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    business = self.get_business(pk)
    serializers = self.serializer_class(business, request.data)
    if serializers.is_valid():
      serializers.save()
      business_list = serializers.data
      response = {
          'data': {
              'business': dict(business_list),
              'status': 'success',
              'message': 'business updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  
  @csrf_exempt
  def post(self, request, format=None):
    print(request.data)
    serializers=self.serializer_class(data=request.data)
    print(serializers)
    if serializers.is_valid():
      serializers.save()
      business=serializers.data
      response = {
          'data': {
              'business': dict(business),
              'status': 'success',
              'message': 'business created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    business = self.get_business(pk)
    business.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
  serializer_class=ProfileSerializer

  def get_profile(self, pk):
    try:
        return Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        raise Http404()
  
  def get(self, request, format=None):
    profile = Profile.objects.all()
    serializers = self.serializer_class(profile, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    profile = self.get_profile(pk)
    serializers = self.serializer_class(profile, request.data)
    if serializers.is_valid():
      serializers.save()
      profile_data = serializers.data
      response = {
          'data': {
              'profile': dict(profile_data),
              'status': 'success',
              'message': 'profile updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
  serializer_class=UserSerializer
  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,format=None):
    users=User.objects.all()
    serializers=self.serializer_class(users, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers=self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()

      users=serializers.data
      response={
        'data':{
          'users':dict(users),
          'status':'success',
          'message':'user created successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk,format=None):
    users=self.get_users(pk)
    serializers=self.serializer_class(users,request.data)
    if serializers.is_valid():
      serializers.save()
      users_list=serializers.data
      response = {
          'data': {
              'users': dict(users_list),
              'status': 'success',
              'message': 'user updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self,request,pk,format=None):
    users=self.get_users(pk)
    users.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(APIView):
  serializer_class=PostSerializer
  def get_post(self, pk):
    try:
        return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404()

  def get(self, request, format=None):
    post = Post.objects.all()
    serializers = self.serializer_class(post, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()

      post = serializers.data
      response = {
          'data': {
              'post': dict(post),
              'status': 'success',
              'message': 'post created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    post = self.get_post(pk)
    serializers = self.serializer_class(post, request.data)
    if serializers.is_valid():
      serializers.save()
      post_data = serializers.data
      response = {
          'data': {
              'post': dict(post_data),
              'status': 'success',
              'message': 'post updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    post = self.get_post(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessSearch(generics.ListAPIView):
  queryset=Business.objects.all()
  serializer_class=BusinessSerializers
  filter_backends=(filters.SearchFilter)
  search_fields=("business_name")
