from django.db import models

class Site(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()
    identifiant = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)