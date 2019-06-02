from django.db import models

ISBN_KEY = "41136_33e4d70318f2a0fe8e9abd311de20f48"
GRADE_CHOICES = (
   ('K4','K4'),
   ('K5','K5'),
   ('01','01'),
   ('02','02'),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
   ('03','03'),
   ('04','04'),
   ('05','05'),
   ('06','06'),
   ('07','07'),
   ('08','08'),
   ('09','09'),
   ('10','10'),
   ('11','11'),
   ('12','12'),
	)
# Create your models here.
#=================================================================================
class TeacherCard(models.Model):
  first_name			=	models.CharField(max_length=30)
  middle_name 		=	models.CharField(max_length=30,blank=True)
  last_name			  =	models.CharField(max_length=30)
  email			      =	models.EmailField()
  room_number     = models.CharField(max_length=30)
  grade           = models.CharField(max_length=6,choices=GRADE_CHOICES)
  section         = models.CharField(max_length=6,blank=True)
  created         = models.DateTimeField(auto_now=True)

  def fullname(self) :
    return "{} {} {}".format(self.first_name,self.middle_name,self.last_name)

  def __str__(self) :
    return self.fullname()

#=================================================================================
class Item(models.Model) :
  teacher   = models.ForeignKey(TeacherCard, on_delete=models.CASCADE)
  number    = models.SmallIntegerField()
  isbn      = models.CharField(max_length=64)
  title     = models.CharField(max_length=2048)
  author    = models.CharField(max_length=1024,blank=True)
  note      = models.CharField(max_length=2048,blank=True)
  
  def __str__(self) :
    return "{} {}".format(self.isbn, self.title)