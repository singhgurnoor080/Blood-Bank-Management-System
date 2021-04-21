from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class register_form(UserCreationForm):
	name = forms.CharField(max_length=35)
	usertype = forms.CharField(max_length=20, widget=forms.Select(choices=Usertype))
	email = forms.EmailField(max_length=250)
	phone_no = forms.CharField(max_length=12)
	pincode = forms.CharField(max_length=12)
	address = forms.CharField(max_length=12)
	blood_type = forms.CharField(max_length=20, widget=forms.Select(choices = blood_choices))
	allegeries = forms.CharField(max_length=20, widget=forms.Select(choices=allergies_choices))
	cardiac_disease = forms.CharField(max_length=20, widget=forms.Select(choices=cardiac_choices))
	bleeding_disorder = forms.CharField(max_length=20, widget=forms.Select(choices=bleeding_disorders_choices))
	hiv = forms.CharField(max_length=20, widget=forms.Select(choices=hbsAg_hcv_hIV_choices))

	class Meta:
		model = User
		fields = ['username','password1','password2','name','usertype','email','phone_no','pincode','address','blood_type','allegeries','cardiac_disease','bleeding_disorder','hiv',]