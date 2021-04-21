from django.test import TestCase

# Create your tests here.
from home.models import person
from django.contrib.auth.models import User
# from django.utils import timezone

class PersonTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('1','vanu@gmail.com','Badal@2000')
        person.objects.create(user=user, name="vanu", usertype="donor", email="user.email", phone_no="9874563210", pincode="781015", address="iiitg", blood_type="A+", allegeries="no", cardiac_disease="no", bleeding_disorder="no", hiv="no")

    def test_Nametest(self):
    	Person = person.objects.get(name='vanu')
    	self.assertEqual(Person.name, 'vanu')
        

    def test_usertype(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.usertype, 'reciepent')
    	self.assertEqual(Person.usertype, 'donor')
        

    def test_Pincode(self):
    	Person = person.objects.get(user='1')
    	field_label = Person._meta.get_field('pincode').verbose_name
    	self.assertEqual(field_label, 'pincode')
        
        

    def test_address(self):
    	Person = person.objects.get(user='1')
    	field_label = Person._meta.get_field('address').verbose_name
    	self.assertEqual(field_label, 'address')
        
        

    def test_blood_type(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.blood_type, 'B+')
    	self.assertEqual(Person.blood_type, 'A+')
        
        

    def test_email(self):
    	Person = person.objects.get(user='1')
    	field_label = Person._meta.get_field('email').verbose_name
    	self.assertEqual(field_label, 'email')
        
        

    def test_phone_no(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.phone_no, '7896541230')
    	self.assertEqual(Person.phone_no, '9874563210')
        
        

    def test_allegeries(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.allegeries, 'yes')
    	self.assertEqual(Person.allegeries, 'no')
        
        

    def test_cardiac_disease(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.cardiac_disease, 'yes')
    	self.assertEqual(Person.cardiac_disease, 'no')
        
        

    def test_bleeding_disorder(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.bleeding_disorder, 'yes')
    	self.assertEqual(Person.bleeding_disorder, 'no')
        
        

    def test_hiv(self):
    	Person = person.objects.get(user='1')
    	self.assertNotEqual(Person.hiv, 'yes')
    	self.assertEqual(Person.hiv, 'no')
        
        

    def test_str(self):
    	Person = person.objects.get(user='1')
    	str_person = '{}'.format(Person.name)
    	self.assertEqual(str(Person), str_person)