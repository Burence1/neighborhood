from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def save_neighborhood(self):
    self.save()

  def delete_neighborhood(self):
    self.delete()

  @classmethod
  def find_neighborhood(cls, name):
    return cls.objects.filter(name__icontains=name)

  @classmethod
  def update_neighborhood(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update

class User(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField()
  neighborhood=models.ForeignKey(Neighborhood,related_name='users', on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_user(self):
    self.save()

  def delete_user(self):
    self.delete()

class Business(models.Model):
  name=models.CharField(max_length=50)
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='business')
  email=models.EmailField()
  neighborhood=models.ForeignKey(Neighborhood,related_name='business',on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    return cls.objects.filter(name__icontains=name)

  @classmethod
  def update_business(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update