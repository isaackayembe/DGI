from django import forms
from .models import Conge

class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['matricule', 'type_conge', 'date_debut', 'date_fin', 'motif']  # 👈 ajoute 'matricule' ici
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre matricule'}),
            'type_conge': forms.Select(attrs={'class': 'form-select'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motif': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'matricule': 'Matricule',
            'type_conge': 'Type de congé',
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin',
            'motif': 'Motif (optionnel)',
        }