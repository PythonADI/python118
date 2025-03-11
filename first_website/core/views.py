from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from core.models import Product
from django.views.generic import (
    DetailView,
    ListView,
    CreateView
)

# Create your views here.
def home_view(request):
    return render(request, "home.html", {
        "products": Product.objects.all()
    })


def about_view(request):
    return render(request, "about.html")


def product_view(request, product_id):
    # print(product_id)
    # if not Product.objects.filter(id=product_id).exists():
    #     return redirect("/")

    # product = Product.objects.get(id=product_id)
    # print(product.title)

    return render(
        request, 
        "product_details.html",
        {
            "product": get_object_or_404(Product, id=product_id)
        }
    )

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "home.html"
    context_object_name = "products"
    paginate_by = 10


class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    fields = "__all__"
    success_url = reverse_lazy("core:product-list")
