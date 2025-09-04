from django.db import models
from django.contrib.auth.models import User
from django import forms

class Employe(models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    service = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"

class Conge(models.Model):
    TYPE_CONGE = [
        ('ANNUEL', 'Congé annuel'),
        ('MALADIE', 'Congé maladie'),
        ('AUTRE', 'Autre'),
    ]

    STATUT = [
        ('EN_ATTENTE', 'En attente'),
        ('APPROUVE', 'Approuvé'),
        ('REJETE', 'Rejeté'),
        ('PLUS_EXPLICATION', 'Plus d\'explications'),  # pour afficher en jaune
    ]

    demandeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conges')
    matricule = models.CharField(max_length=20, blank=True, null=True)  # Nouveau champ
    type_conge = models.CharField(max_length=20, choices=TYPE_CONGE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT, default='EN_ATTENTE')
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.demandeur.username} - {self.type_conge} ({self.statut})"


class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ["type_conge", "date_debut", "date_fin", "motif"]
        widgets = {
            "date_debut": forms.DateInput(attrs={"type": "date"}),
            "date_fin": forms.DateInput(attrs={"type": "date"}),
        }