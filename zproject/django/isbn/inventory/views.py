from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
import requests as req
from datetime import date
# Create your views here.

#=====================================
def isbn_api(bookid) :
  h = {'Authorization': ISBN_KEY }
  resp = req.get("https://api2.isbndb.com/book/{}".format(bookid), headers=h)
  return(resp.json())
#=====================================
def teacher(request,email) :
  result={}

  if "delete_rec" in request.POST :
    Item.objects.get(id=request.POST["delete_rec"]).delete()
    tcard =  TeacherCard.objects.get(email=email) 
    result["teacher_form"] = TeacherCardForm(instance=tcard)
    result["item_list"] = Item.objects.filter(teacher__id=tcard.id)
    result["teacher_card"] = tcard
  
  if "update_rec" in request.POST :
    item = Item.objects.get(id=request.POST["update_rec"])
    item.number = request.POST["rec_number"]
    item.title  = request.POST["rec_title"]
    item.author = request.POST["rec_author"]
    item.note  = request.POST["rec_note"]
    item.save()    


  if 'save_rec' in request.POST :
    teacher = TeacherCard.objects.get(id=int(request.POST["teacherId"]))
    if "scanISBN" in request.POST :
      isbn = request.POST["scanISBN"]
      items = Item.objects.filter(isbn=isbn) 
      if items :
        items[0].number += 1
        items[0].save()
      else :
        item = Item()
        bk = isbn_api(isbn)
        item.teacher = teacher 
        item.isbn = isbn
        item.number = 1
        result["bk"] = bk
        try:
          item.title = bk["book"]["title_long"]
          item.author = bk["book"]["authors"]
        except:
          pass
        item.save()

  try:
    tcard =  TeacherCard.objects.get(email=email) 
    result["teacher_form"] = TeacherCardForm(instance=tcard)
    result["item_list"] = Item.objects.filter(teacher__id=tcard.id).order_by("-id")
    result["teacher_card"] = tcard
  except:
    return redirect("logon")
  result["item_form"] = ItemForm()

  return  render(request,'teacher.html',context=result)
#=====================================
def report(request,email) :
  result = {}
  tcard = TeacherCard.objects.get(email=email) 
  result['date_today'] = date.today()
  result["teacher"] =  tcard
  result["item_list"] = Item.objects.filter(teacher__id=tcard.id).order_by("-id")
  return  render(request,'report.html',context=result)
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
