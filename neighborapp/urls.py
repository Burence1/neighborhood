from . import views
from django.conf import settings
from django.urls import path, re_path


urlpatterns=[
  path('api/neighbors/',views.NeighborhoodList.as_view(),name='neighbor'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/users/update/<int:pk>/',views.UserList.as_view(),name='update_users'),
  path('api/users/delete/<int:pk>/',views.UserList.as_view(),name='delete_users'),
]