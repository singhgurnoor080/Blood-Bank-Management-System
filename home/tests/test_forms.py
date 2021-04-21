from django.test import TestCase

from home.forms import register_form

class register_formTestCase(TestCase):

	def test_name(self):
		name_p = "vanu"
		form = register_form(data={'name': name_p})
		print("user name test case passed...")
		self.assertFalse(form.is_valid())

	def test_usertype(self):
		usertype_p = "reciepent"
		form = register_form(data={'usertype': usertype_p})
		self.assertFalse(form.is_valid())

	def test_username(self):
		username_p = "vanu_123"
		form = register_form(data={'username': username_p})
		self.assertFalse(form.is_valid())

	def test_allFields_correct(self):
		username_p = "vanu_123"
		password1_p = "Badal@2000"
		password2_p = "Badal@2000"
		name_p = "vanu"
		usertype_p = "reciepent"
		email_p = "vanu@gmail.com"
		phone_no_p = "9874563210"
		pincode_p = "781015"
		address_p = "iiitg"
		blood_type_p = "A+"
		allegeries_p = "no"
		cardiac_disease_p = "no"
		bleeding_disorder_p = "no"
		hiv_p = "no"

		form = register_form(data={'username': username_p, 'password1': password1_p, 'password2': password2_p, 'name': name_p, 'usertype': usertype_p, 'email': email_p, 'phone_no': phone_no_p, 'pincode': pincode_p, 'address': address_p, 'blood_type': blood_type_p, 'allegeries': allegeries_p, 'cardiac_disease': cardiac_disease_p, 'bleeding_disorder': bleeding_disorder_p, 'hiv': hiv_p})
		print("all field testcase passed")
		self.assertTrue(form.is_valid())

	def test_verification_password_wrong(self):
		username_p = "vanu_123"
		password1_p = "Badal@2000"
		password2_p = "Badal@000"
		name_p = "vanu"
		usertype_p = "reciepent"
		email_p = "vanu@gmail.com"
		phone_no_p = "9874563210"
		pincode_p = "781015"
		address_p = "iiitg"
		blood_type_p = "A+"
		allegeries_p = "no"
		cardiac_disease_p = "no"
		bleeding_disorder_p = "no"
		hiv_p = "no"

		form = register_form(data={'username': username_p, 'password1': password1_p, 'password2': password2_p, 'name': name_p, 'usertype': usertype_p, 'email': email_p, 'phone_no': phone_no_p, 'pincode': pincode_p, 'address': address_p, 'blood_type': blood_type_p, 'allegeries': allegeries_p, 'cardiac_disease': cardiac_disease_p, 'bleeding_disorder': bleeding_disorder_p, 'hiv': hiv_p})
		print("password confirmation test case passed")
		self.assertFalse(form.is_valid())

	def test_email_not_correct_format(self):
		username_p = "vanu_123"
		password1_p = "Badal@2000"
		password2_p = "Badal@2000"
		name_p = "vanu"
		usertype_p = "reciepent"
		email_p = "vanu@.com"
		phone_no_p = "9874563210"
		pincode_p = "781015"
		address_p = "iiitg"
		blood_type_p = "A+"
		allegeries_p = "no"
		cardiac_disease_p = "no"
		bleeding_disorder_p = "no"
		hiv_p = "no"

		form = register_form(data={'username': username_p, 'password1': password1_p, 'password2': password2_p, 'name': name_p, 'usertype': usertype_p, 'email': email_p, 'phone_no': phone_no_p, 'pincode': pincode_p, 'address': address_p, 'blood_type': blood_type_p, 'allegeries': allegeries_p, 'cardiac_disease': cardiac_disease_p, 'bleeding_disorder': bleeding_disorder_p, 'hiv': hiv_p})
		print("Email test case passed")
		self.assertFalse(form.is_valid())