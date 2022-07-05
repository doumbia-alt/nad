from apps import views
from django.urls import path, include



urlpatterns = [

path(r'', views.index, name="index"),
path(r'preinscription/', views.preinscription, name='preinscription'),

path(r'contact/', views.contact, name='contact'),
path(r'apropos/', views.apropos, name='apropos'),
path(r'actualite/', views.actualite, name='actualite'),
path(r'ad/', views.ad, name='ad'),
path(r'ida/', views.ida, name='ida'),
path(r'gbat/', views.gbat, name='gbat'),
path(r'fcge/', views.fcge, name='fcge'),
path(r'gescom/', views.gescom, name='gescom'),
path(r'rhcopm/', views.rhcom, name='rhcom'),
path(r'th/', views.th, name='th'),
path(r'log/', views.log, name='log'),

 ]