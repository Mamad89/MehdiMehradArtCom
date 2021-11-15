from django.shortcuts import render
from .models import Product


# Create your views here.


def show_products_page(request):
	product = Product(request.POST or None)
	content = {
		"name" : product.name,
		"price" : product.price,
		"distribution" : product.distribution
	}
	return render(request, 'app_products/products.html', content)
