from django import forms
from django.contrib.auth.models import User
from django.forms import *
from .models import  * 
from datetime import datetime 

#===============================
class TeacherCardForm(ModelForm) :
	class Meta:
		model = TeacherCard
		exclude = [ 'created'] 
#===============================
class ItemForm(ModelForm) :
	class Meta:
		model = Item
		fields = ['number','isbn']
