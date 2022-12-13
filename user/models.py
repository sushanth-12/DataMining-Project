from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)


class PhishingModel(models.Model):
    attack_type=models.CharField(max_length=100)
    text=models.CharField(max_length=500)