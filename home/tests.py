from django.test import TestCase
from home.models import *
from django.contrib.auth.models import User
from django.utils import timezone
# from django.core.urlresolvers import reverse
from home.forms import register_form

# models test
# class personTest(TestCase):

#     def create_person(self, user="badal_123", name="badal", usertype="donor", email="kumarbadal208@gmail.com", phone_no="9874563210", pincode="781015", address="iiitg", blood_type="A+", allegeries="no", cardiac_disease="no", bleeding_disorder="no", hiv="no"):
#         return person.objects.create(user="user", name="name", usertype="usertype", email="email", phone_no="phone_no", pincode="pincode", address="address", blood_type="blood_type", allegeries="allegeries", cardiac_disease="cardiac_disease", bleeding_disorder="bleeding_disorder", hiv="hiv", created_at=timezone.now())

#     def test_person_creation(self):
#         w = self.create_person()
#         self.assertTrue(isinstance(w, person))
#         self.assertEqual(w.__unicode__(), w.user)




