import django_filters
from .models import *

class donor_filter(django_filters.FilterSet):
	class Meta:
		model = person
		fields = ['blood_type','pincode']