from django.contrib import admin
from .models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    list_display  = ('nom_entreprise', 'email', 'telephone', 'ville', 'statut', 'cree_par', 'date_creation')
    list_filter   = ('statut', 'secteur', 'ville')
    search_fields = ('nom_entreprise', 'email', 'ville')