from django.db import models

class Livraison(models.Model):
    contact = models.CharField(max_length=255, verbose_name="Numéro mobile ou e-mail")
    adresse = models.TextField(verbose_name="Adresse")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Livraison'
        verbose_name_plural = 'Livraisons'

    def __str__(self):
        return self.contact
