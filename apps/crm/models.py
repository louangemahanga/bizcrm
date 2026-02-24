from django.db import models
from django.contrib.auth.models import User 


class Prospect(models.Model):

    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('contacte', 'Contacté'),
        ('interesse', 'Intéressé'),
        ('negocia', 'En négociation'),
        ('client', 'Client'),
        ('perdu', 'Perdu'),
    ]

    SECTEUR_CHOICES = [
        ('commerce', 'Commerce'),
        ('industrie', 'Industrie'),
        ('services', 'Services'),
        ('tech', 'Technologie'),
        ('sante', 'Santé'),
        ('education', 'Éducation'),
        ('autre', 'Autre'),
    ]

    nom_entreprise = models.CharField(max_length=200)
    email          = models.EmailField(blank=True, null=True)
    telephone      = models.CharField(max_length=20, blank=True, null=True)
    adresse        = models.TextField(blank=True, null=True)
    ville          = models.CharField(max_length=100, blank=True, null=True)
    secteur        = models.CharField(max_length=50, choices=SECTEUR_CHOICES, default='autre')
    statut         = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')
    notes          = models.TextField(blank=True, null=True)
    date_creation  = models.DateTimeField(auto_now_add=True)
    date_modif     = models.DateTimeField(auto_now=True)
    cree_par       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prospects')

    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'Prospect'
        verbose_name_plural = 'Prospects'

    def __str__(self):
        return self.nom_entreprise



class Prospect(models.Model):

    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('contacte', 'Contacté'),
        ('interesse', 'Intéressé'),
        ('negocia', 'En négociation'),
        ('client', 'Client'),
        ('perdu', 'Perdu'),
    ]

    SECTEUR_CHOICES = [
        ('commerce', 'Commerce'),
        ('industrie', 'Industrie'),
        ('services', 'Services'),
        ('tech', 'Technologie'),
        ('sante', 'Santé'),
        ('education', 'Éducation'),
        ('autre', 'Autre'),
    ]

    nom_entreprise = models.CharField(max_length=200)
    email          = models.EmailField(blank=True, null=True)
    telephone      = models.CharField(max_length=20, blank=True, null=True)
    adresse        = models.TextField(blank=True, null=True)
    ville          = models.CharField(max_length=100, blank=True, null=True)
    secteur        = models.CharField(max_length=50, choices=SECTEUR_CHOICES, default='autre')
    statut         = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')
    notes          = models.TextField(blank=True, null=True)
    date_creation  = models.DateTimeField(auto_now_add=True)
    date_modif     = models.DateTimeField(auto_now=True)
    cree_par       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prospects')

    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'Prospect'
        verbose_name_plural = 'Prospects'

    def __str__(self):
        return self.nom_entreprise