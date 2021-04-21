from django.test import TestCase
from django.urls import reverse
from home.models import *
from home.views import *
from django.test import Client
from django.http import response
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import random, datetime


class HomeBase(TestCase):
	@classmethod
	def test_view_url_exists_at_desired_location(self):
		c = Client()
		response = c.get('/admin_login/')

	def test_login_page(self):
		login = self.client.login(username = 'admin',password='admin')
		response = self.client.get('//admin_login/')
		# print(response.status_code)
		self.assertEqual(response.status_code,200)

	def test_login_page_user(self):
		login = self.client.login(username = 'ashmit_123',password='Badal@2000')
		response = self.client.get('//search/')
		self.assertEqual(response.status_code,200)

	def test_login_page_user(self):
		login = self.client.login(username = 'ashmit_123',password='Badal@2000')
		response = self.client.get('//homepage/')
		self.assertEqual(response.status_code,200)