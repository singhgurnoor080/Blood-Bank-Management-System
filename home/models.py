from django.db import models
from django.contrib.auth.models import User

Usertype = [('donor','donor'),('reciepent','reciepent')]
blood_choices = [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]

allergies_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]

cardiac_choices=[
        ("yes","Yes"),
        ("no", "No"),
    ]

bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]

hbsAg_hcv_hIV_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]


 

class person(models.Model):
	Usertype = [('donor','donor'),('reciepent','reciepent')]
	blood_choices = [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]

	allergies_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]

	cardiac_choices=[
        ("yes","Yes"),
        ("no", "No"),
    ]

	bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]

	hbsAg_hcv_hIV_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]



	user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
	name = models.CharField(max_length=35, blank = False)
	usertype = models.CharField(max_length=20, choices=Usertype)
	email = models.EmailField(max_length=250, blank=False)
	phone_no = models.CharField(max_length=12, blank=False)
	pincode = models.CharField(max_length=12, blank=False)
	address = models.CharField(max_length=12, blank=False)
	blood_type = models.CharField(max_length=20, choices=blood_choices)
	allegeries = models.CharField(max_length=20, choices=allergies_choices)
	cardiac_disease = models.CharField(max_length=20, choices=cardiac_choices)
	bleeding_disorder = models.CharField(max_length=20, choices=bleeding_disorders_choices)
	hiv = models.CharField(max_length=20, choices=hbsAg_hcv_hIV_choices)

	def __str__(self):
		return self.name

 
