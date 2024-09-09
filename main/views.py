from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    context = {
        'nama': 'Alyssa Layla Sasti',
        'kelas': 'PBP D',
        'npm': 2306152052,
        'products': [ 
            {'name': 'Dimsum Mozarella', 'price': 20000, 'quantity': 5, 'description': 'Dimsum dengan keju Mozarella meleleh di atasnya wow enak', 'category': 'Makanan'},
            {'name': 'Charger HP', 'price': 100000, 'quantity': 8, 'description': 'Charge HP dijamin Original!', 'category': 'Elektronik'},
            {'name': 'Hoodie', 'price': 50000, 'quantity': 3, 'description': 'Hoodie Oversize paling keren se-UI', 'category': 'Pakaian'},
            ],
    }

    return render(request, "main.html", context)
