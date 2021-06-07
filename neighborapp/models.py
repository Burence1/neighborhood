from os import name
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighborhood(models.Model):
  name = models.CharField(max_length=50)
  hood_desc=models.TextField()
  location = models.CharField(max_length=50)
  image=CloudinaryField('hood image',null=True)

  def __str__(self):
    return self.name

  def save_neighborhood(self):
    self.save()

  def delete_neighborhood(self):
    self.delete()

  @classmethod
  def find_neighborhood(cls, hood_id):
    return cls.objects.filter(id=hood_id)

  @classmethod
  def update_neighborhood(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update

class Profile(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  name=models.CharField(max_length=50)
  profile_pic=CloudinaryField('profile')
  email=models.EmailField()
  neighborhood=models.ForeignKey(Neighborhood,related_name='occupants', on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.name

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)
  
  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  def save_user(self):
    self.save()

  def delete_user(self):
    self.delete()

class Business(models.Model):
  business_name=models.CharField(max_length=50)
  business_desc=models.TextField()
  image=CloudinaryField('business image',null=True)
  profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='business_user',null=True)
  business_email=models.EmailField()
  neighborhood=models.ForeignKey(Neighborhood,related_name='business_hood',on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.business_name

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    return cls.objects.filter(business_name__icontains=name)

  @classmethod
  def update_business(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update

class Post(models.Model):
  post_name=models.CharField(max_length=100)
  post_content=models.TextField()
  pub_date=models.DateTimeField(auto_now_add=True)
  profile=models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='post',null=True)
  hood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='post_hood',null=True)

  def __str__(self):
    return self.post_name