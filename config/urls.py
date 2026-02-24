from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/',   admin.site.urls),
    path('users/',   include('apps.users.urls')),
    path('crm/',     include('apps.crm.urls')),
    path('',         lambda request: redirect('crm:dashboard')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)