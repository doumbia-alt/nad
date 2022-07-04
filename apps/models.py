from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
 nom = models.TextField()
 prenom = models.TextField(null=True , blank=True)
 email = models.EmailField(null=True , blank=True)
 sujet = models.TextField()
 message = models.TextField()
 date = models.DateTimeField(default=timezone.now)
 #likes = models.IntegerField(default=0)
 def __str__(self):
	 return self.nom

class Pre_inscription(models.Model):
 nom = models.TextField()
 prenom = models.TextField()
 email = models.EmailField(null=True , blank=True)
 phone = models.CharField(max_length=12)
 ecole = models.TextField()
 formation = models.TextField()
 filiere = models.TextField()
 date = models.DateTimeField(default=timezone.now)
 #likes = models.IntegerField(default=0)
    
 def __str__(self):
	 return self.nom