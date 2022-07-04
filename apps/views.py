from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def fcge(request):
    return render(request, 'fcge.html', {})

def ad(request):
    return render(request, 'ad.html', {})

def gbat(request):
    return render(request, 'gbat.html', {})

def gescom(request):
    return render(request, 'gescom.html', {})

def log(request):
    return render(request, 'log.html', {})

def ida(request):
    return render(request, 'ida.html', {})

def apropos(request):
    return render(request, 'a_propos.html', {})

def contact(request):
    
    if request.method == "POST":
        #context = {'success': False}
        fistname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(fistname,lastname,email,subject,message)
        voir = Contact(nom = fistname, prenom = lastname, email = email , sujet = subject , message = message)
        voir.save()
    return render(request, 'contact.html', {})

def preinscription(request):
    
    if request.method == "POST":
        #context = {'success': False}
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email'] 
        phone = request.POST['phone']
        schoolId = request.POST['schoolId']
        trainingId = request.POST['trainingId']
        facultyId = request.POST['facultyId']
        
        print(firstname,lastname,email,phone,schoolId,trainingId,facultyId)
        voir = Pre_inscription(nom = firstname, prenom = lastname, email = email , telephone = phone , ecole = schoolId , formation = trainingId , filiere = facultyId)
        voir.save()
    return render(request, 'pre-inscription.html', {})

def rhcom(request):
    return render(request, 'rhcom.html', {})

def th(request):
    return render(request, 'th.html', {})


def actualite(request):
    return render(request, 'actualite.html', {})