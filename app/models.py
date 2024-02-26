from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()
    def _str_(self):
        return self.username.username

class Pgs(models.Model):
    pg_name=models.CharField(max_length=100)
    pg_address=models.CharField(max_length=500)
    pg_pic=models.ImageField(default='ntr.jpg')
    pg_cost=models.IntegerField()

    def _str_(self):
        return self.pg_name

class Booking(models.Model):
    pg_name=models.OneToOneField(Pgs,on_delete=models.CASCADE)
    customer=models.CharField(max_length=100)
    age=models.IntegerField()
    option_menu=(('Male','Male'),('Female','Female'))
    gender = models.CharField(max_length=200, choices=option_menu)
    option_menu1=(('Student','Student'),('Job','Job'))
    profession=models.CharField(max_length=300,choices=option_menu1)
    phone_number=models.CharField(max_length=20)
    address=models.TextField()
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    aadhaar_card=models.FileField()
    photo=models.ImageField()

    def _str_(self):
        return self.pg_name.pg_name

class Payment(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
