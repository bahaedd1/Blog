from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now())

class Details(models.Model):
    iduser = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userdet')
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    img = models.ImageField(blank =True)
    #champ = models.type(attrb,default= "" ou null = True)

class Article(models.Model):
    iduser = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(blank = True)
    date = models.DateTimeField(default=datetime.now())