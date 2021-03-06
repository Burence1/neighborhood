from . import views
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken



urlpatterns=[
  #post and get urls
  path('api/hood/',views.NeighborhoodList.as_view(),name='neighbor'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/profile/',views.ProfileList.as_view(),name='profiles'),
  path('api/post/',views.PostList.as_view(),name='post'),
  #update urls
  path('api/update/profile/<int:pk>/',views.ProfileList.as_view(),name='update_profile'),
  path('api/update/users/<int:pk>/',views.UserList.as_view(),name='update_users'),
  re_path('api/update/business/(?P<pk>[0-9]+)/',views.BusinessList.as_view(),name='update_business'),
  path('api/update/hood/<int:pk>/',views.NeighborhoodList.as_view(),name='update_neighbors'),
  path('api/update/post/<int:pk>/',views.PostList.as_view(),name='update_post'),
  #delete urls
  path('api/delete/users/<int:pk>/',views.UserList.as_view(),name='delete_users'),
  re_path('api/delete/hood/(?P<pk>[0-9]+)/',views.NeighborhoodList.as_view(),name='delete_neighbors'),
  path('api/delete/business/<int:pk>/',views.BusinessList.as_view(),name='delete_business'),
  path('api/delete/post/<int:pk>/',views.PostList.as_view(),name='delete_post'),


  #search urls
  path('api/business/list/<name>',views.BusinessSearchList.as_view(),name='search'),
  # path('loginuser/', views.LoginUser.as_view(), name="loginuser"),
  path('authlogin/', ObtainAuthToken.as_view(), name="authlogin"),

  #singleitems
  path('api/single-hood/<int:pk>/',views.singleHood.as_view()),
  path('api/single-business/<int:pk>/',views.singleBusiness.as_view()),
  path('api/single-post/<int:pk>/',views.singlePost.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)