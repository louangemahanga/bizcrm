from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('dashboard/',                         views.dashboard,              name='dashboard'),
    path('prospects/',                         views.prospect_list,          name='prospect_list'),
    path('prospects/ajouter/',                 views.prospect_create,        name='prospect_create'),
    path('prospects/export/',                  views.export_excel,           name='export_excel'),
    path('prospects/import/',                  views.import_csv,             name='import_csv'),
    path('prospects/modele-csv/',              views.telecharger_modele_csv, name='telecharger_modele_csv'),
    path('prospects/<int:pk>/',                views.prospect_detail,        name='prospect_detail'),
    path('prospects/<int:pk>/modifier/',       views.prospect_update,        name='prospect_update'),
    path('prospects/<int:pk>/supprimer/',      views.prospect_delete,        name='prospect_delete'),
    path('prospects/<int:pk>/relance/',        views.envoyer_relance,        name='envoyer_relance'),  # ← cette ligne
]