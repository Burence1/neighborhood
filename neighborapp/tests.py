from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.


class ProfileClass(TestCase):
  def setUp(self):
    self.user = User(username='burens')
    self.user.save()
    self.profile = Profile(user=self.user, profile_pic='lol.png',name="burens",neighborhood='karen',email='mail@gmail.com')

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.profile, Profile))

  def test_save_profile(self):
    self.new_profile = Profile(user=self.kanosa, url='www.lol.com', profile_pic='lol.png',
                               bio='awesome', location='kenya', email='mail@gmail.com')
    self.new_profile.save_profile()
    profiles = Profile.objects.all()
    self.assertEqual(len(profiles), 1)

class BusinessClass(TestCase):
  def setUp(self):
    self.new_profile.save()
    self.business=Business.objects.create(profile=self.burens,business_name="moringa",business_desc="school",image="tech.png",business_email="mail1@gmail.com",neighborhood="karen")

  def tearDown(self):
    Business.objects.all().delete()
    Profile.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.business, Business))

  def test_save_business(self):
    self.business.save_business()
    total_business = Business.objects.all()
    self.assertEqual(len(total_business), 1)

  def test_delete_business(self):
    self.business.save_business()
    business=Business.objects.all()
    self.assertEqual(len(business),1)
    self.business.delete_business()
    total_business=Business.objects.all()
    self.assertTrue(len(total_business)==0)

  
class NeighborhoodClass(TestCase):
  def setUp(self):
    self.hood = Neighborhood.objects.create(name="karen",hood_desc="school", image="tech.png", location="nairobi")

  def tearDown(self):
    Neighborhood.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.hood, Neighborhood))

  def test_save_neighborhood(self):
    self.hood.save_neighborhood()
    total_hoods =Neighborhood.objects.all()
    self.assertEqual(len(total_hoods), 1)

  def test_delete_business(self):
    self.hood.save_neighborhood()
    hoods = Neighborhood.objects.all()
    self.assertEqual(len(hoods), 1)
    self.hood.delete_neighborhood()
    total_hoods = Neighborhood.objects.all()
    self.assertTrue(len(total_hoods) == 0)