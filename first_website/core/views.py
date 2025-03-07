from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product

# Create your views here.
def home_view(request):
    return render(request, "home.html", {
        "products": Product.objects.all()
    })


def about_view(request):
    return render(request, "about.html")
