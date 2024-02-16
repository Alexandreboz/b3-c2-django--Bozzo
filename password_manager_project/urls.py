"""
URL configuration for password_manager_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from password_manager import views as pm_views

urlpatterns = [
    path('', pm_views.liste_sites, name='liste_sites'),
    path('ajouter/', pm_views.ajouter_site, name='ajouter_site'),
    path('modifier/<int:site_id>/', pm_views.modifier_site, name='modifier_site'),
    path('supprimer/<int:site_id>/', pm_views.supprimer_site, name='supprimer_site'),
    path('<int:site_id>/', pm_views.detail_site, name='detail_site'),
    path('inscription/', pm_views.inscription, name='inscription'),
    path('connexion/', pm_views.connexion, name='connexion'),
    path('deconnexion/', pm_views.deconnexion, name='deconnexion'),
    path('connexion/', include('django.contrib.auth.urls')),
]

