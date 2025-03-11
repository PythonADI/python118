from django.urls import path

from core.views import (
    about_view,
    ProductDetailView,
    ProductListView,
    ProductCreateView,
)

app_name = "core"

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("about/", about_view, name="about"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-details"),
    path("products/create", ProductCreateView.as_view(), name="product-create"),

]
