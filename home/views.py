from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .filters import *

# Create your views here.

def homebase(request):
	return render(request,'home/homebase.html')
	
def about(request):
	return render(request,'home/about.html')

def user_about(request):
	return render(request,'home/user_about.html')

def user_contact(request):
	return render(request,'home/user_contact.html')

def contact(request):
	return render(request,'home/contact.html')	

@login_required(login_url = 'login')
def homepage(request):
	if request.user.groups.exists:
		group = request.user.groups.all()[0].name
		if group=='admin':
			return redirect('admin_login')
	print(request.user)
	person_log = person.objects.get(user= request.user)
	print(person_log)



	return render(request,'home/homepage.html')

def register_person(request):
	form = register_form()
	if request.method=='POST':
		form = register_form(request.POST)
		if form.is_valid():
			person_add = form.save()
			group_donor = Group.objects.get(name='donor')
			group_reciepent = Group.objects.get(name='reciepent')
			usertype = form.cleaned_data.get('usertype')
			print(usertype)
			if usertype=='donor':
				person_add.groups.add(group_donor)
			if usertype=='reciepent':
				person_add.groups.add(group_reciepent)

			person.objects.create(
				user = person_add,
				email = form.cleaned_data.get('email'),
				name = form.cleaned_data.get('name'),
				usertype = form.cleaned_data.get('usertype'),
				phone_no = form.cleaned_data.get('phone_no'),
				pincode = form.cleaned_data.get('pincode'),
				address = form.cleaned_data.get('address'),
				blood_type = form.cleaned_data.get('blood_type'),
				allegeries = form.cleaned_data.get('allegeries'),
				cardiac_disease = form.cleaned_data.get('cardiac_disease'),
				bleeding_disorder = form.cleaned_data.get('bleeding_disorder'),
				hiv = form.cleaned_data.get('hiv'),
				)

	return render(request,'home/base.html',{'form':form})


@logging_in
def login_person(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('inputPassword')
		user = authenticate(request,username=username,password=password)
		print(user)

		if user is not None:
			login(request,user)
			return redirect('homepage')
		# else:
		# 	messages.info(request,'Failed')

	return render(request,'home/login.html')

def logout_person(request):
	logout(request)
	return redirect('login')

@login_required(login_url = 'login')
def search(request):
	donors = person.objects.filter(usertype='donor')
	donor_search = donor_filter(request.GET, queryset=donors)
	if request.method == 'GET':
		donors = donor_search.qs
	return render(request,'home/search.html',{'donors': donors, 'donor_search': donor_search})

@login_required(login_url = 'login')
@person_admin(allowed_roles=['admin'])
def admin_login(request):
	donors = person.objects.filter(usertype='donor')
	reciepents = person.objects.filter(usertype='reciepent') 
	if request.method=='POST':
		cu = request.POST.get('current_user')
		current_user = person.objects.get(id=cu)
		current_user.delete()
		return redirect('admin_login')
	return render(request,'home/admin.html',{'donors': donors, 'reciepent': reciepents})

def location(request):
	return render(request,'home/location.html')