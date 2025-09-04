from django.contrib import admin
from .models import Employe

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ("matricule", "nom", "prenom", "fonction", "service")
    search_fields = ("nom", "prenom", "matricule")

