from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Title(models.Model):
    icon= models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

class carousel(models.Model):
    Image = models.ImageField(upload_to='assets', null = True)
    Img_title = models.CharField(max_length=100, null=True)
    Img_desc = models.CharField(max_length=500, null=True)

class About(models.Model):
    img1=models.ImageField(upload_to='assets')
    mission= models.CharField(max_length=2000)
    history= models.CharField(max_length=4000)

    def __str__(self):
        return self.mission

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    
    def __str__(self):

        return self.name

class Faculties(models.Model):
    img= models.ImageField(upload_to='assets')
    name=models.CharField(max_length=100)
    level= models.CharField(max_length=200)
    about= models.TextField(max_length=500)
    twitter= models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    insta= models.CharField(max_length=100)
    linkdln= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Other(models.Model):
    logo= models.ImageField(upload_to='assets')
    address= models.CharField(max_length=200)
    phone= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    insta=models.CharField(max_length=100)
    facebook= models.CharField(max_length=100)
    linkdln= models.CharField(max_length=100)

class News(models.Model):
    updates=models.CharField(max_length=200)
    link= models.CharField(max_length=200)
    date= datetime.datetime.now()
    file= models.FileField(upload_to='assets')

    def __str__(self):
        return self.updates
        
class Events(models.Model):
    updates=models.CharField(max_length=200)
    link= models.CharField(max_length=200)
    date= datetime.datetime.now()
    file= models.FileField(upload_to='assets')

    def __str__(self):
        return self.updates


class Faculty_Detail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    father= models.CharField(max_length=100)
    aadhar= models.CharField(max_length=200)
    img= models.ImageField(upload_to='assets',default="static/img/logo.png")

    def __str__(self):
        return self.name



class Student_detail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mother= models.CharField(max_length=100)
    father= models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    phone= models.CharField(max_length=100)
    standerd= models.CharField(max_length=100)
    aadhar= models.CharField(max_length=100)
    year= models.CharField(max_length=100)
    pre_standerd=models.CharField(max_length=100)
    img=models.ImageField(upload_to='assets',default="static/img/logo.png")
    fee_status= models.TextField(max_length=10000,default='0')
    email = models.CharField(max_length=100)

    def __str__(self):
        template='{0.name} {0.standerd}'
        return template.format(self)

    

class Academy(models.Model):
    fee_structure=models.FileField(upload_to='assets')
    book_syllabus= models.FileField(upload_to='assets')
    course=models.FileField(upload_to='assets')

class Gallery(models.Model):
    img= models.ImageField(upload_to='assets')

    



