from django.shortcuts import render

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
    return render(request, 'contact.html', {})

def preinscription(request):
    return render(request, 'pre_inscription.html', {})

def rhcom(request):
    return render(request, 'rhcom.html', {})

def th(request):
    return render(request, 'th.html', {})


def actualite(request):
    return render(request, 'actualite.html', {})