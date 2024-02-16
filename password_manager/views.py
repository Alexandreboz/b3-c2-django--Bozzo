from django.shortcuts import render, redirect, get_object_or_404
from .models import Site
from .forms import SiteForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'liste_sites.html', {'sites': sites})

def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()
    return render(request, 'ajouter_site.html', {'form': form})

def modifier_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm(instance=site)
    return render(request, 'modifier_site.html', {'form': form, 'site': site})

def supprimer_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        site.delete()
        return redirect('liste_sites')
    return render(request, 'supprimer_site.html', {'site': site})

def detail_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'detail_site.html', {'site': site})
def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_sites')
    else:
        form = UserCreationForm()
    return render(request, 'registration/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('liste_sites')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return render(request, 'registration/deconnexion.html')