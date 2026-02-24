from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/',        views.login_view,  name='login'),
    path('logout/',       views.logout_view, name='logout'),
    path('utilisateurs/', views.user_list,   name='user_list'),
    path('utilisateurs/ajouter/', views.user_create, name='user_create'),
]