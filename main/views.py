from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    context = {
        'name': 'Dimsum Mozarella',
        'price': 20000,
        'description': 'Dimsum dengan keju Mozarella meleleh di atasnya wow enak'
    }

    return render(request, "main.html", context)
