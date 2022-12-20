from django.db import models
from django.db.models import Model
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField( max_length=64,unique=True)
    password_hash=models.CharField(max_length=64)
    role=models.CharField(max_length=10)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password,method='sha256')

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    

class Group(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50, unique=True)
    creator_id=models.IntegerField()
    

class Group_member(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    groupname = models.ForeignKey(Group,on_delete=models.CASCADE)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)