from django import forms
from .models import Prospect


class ProspectForm(forms.ModelForm):
    class Meta:
        model  = Prospect
        fields = [
            'nom_entreprise', 'email', 'telephone',
            'adresse', 'ville', 'secteur', 'statut', 'notes'
        ]
        widgets = {
            'nom_entreprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom entreprise'}),
            'email':          forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telephone':      forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'adresse':        forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ville':          forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'secteur':        forms.Select(attrs={'class': 'form-select'}),
            'statut':         forms.Select(attrs={'class': 'form-select'}),
            'notes':          forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }