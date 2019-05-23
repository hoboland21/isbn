from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# Create your views here.

#=====================================
def teacher(request,email) :
  result={}
  try:
    tcard =  TeacherCard.objects.get(email=email) 
    result["teacher_card"] = TeacherCardForm(instance=tcard)
  except:
    return redirect("logon")

  return  render(request,'teacher.html',context=result)
#=====================================
def logon(request) :
  result={}
  if "email" in request.POST :
    tcard =  TeacherCard.objects.filter(email=request.POST["email"]) 
    
    if tcard :
      return redirect("teacher",tcard[0].email)
    else :
      result["teacher_form"] = TeacherCardForm()
  if "register" in request.POST :
    tc = TeacherCard()
    input_form = TeacherCardForm(request.POST,instance=tc)
    if input_form.is_valid() :
      tc.save()
      return redirect("teacher",tc.email)

  return  render(request,'logon.html',context=result)
#=====================================
