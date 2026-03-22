from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Livraison

def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        contact = request.POST.get('contact', '').strip()
        adresse = request.POST.get('adresse', '').strip()

        if contact and adresse:
            Livraison.objects.create(contact=contact, adresse=adresse)
            return redirect('https://web.facebook.com/')
        else:
            messages.error(request, "Veuillez remplir tous les champs.")
        return redirect('index')

    return redirect('index')
