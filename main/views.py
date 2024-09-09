from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    context = {
        'name': 'Dimsum Mozarella',
        'price': 20000,
        'descriprion': 'Dimsum dengan keju Mozarella meleleh di atasnya'
    }

    return render(request, "main.html", context)
