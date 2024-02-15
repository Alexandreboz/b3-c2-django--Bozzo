from audioop import reverse
from django.db import models

class Site(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()
    identifiant = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail_site', kwargs={'site_id': self.pk})