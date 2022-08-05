from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Contact)
@admin.site.register(Cre_inscription):
list_display = ('nom','prenom','email','phone','ecole','formation','filiere','date')
