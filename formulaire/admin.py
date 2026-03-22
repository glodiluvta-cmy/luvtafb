from django.contrib import admin
from .models import Livraison

@admin.register(Livraison)
class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('contact', 'adresse', 'created_at')
    search_fields = ('contact', 'adresse')
    list_filter = ('created_at',)
