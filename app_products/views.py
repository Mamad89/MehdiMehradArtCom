from django.shortcuts import render
from .models import Product


# Create your views here.


def show_products_page(request):
	products = Product.objects.all()
	content = {
		"products" : products
	}
	return render(request, 'app_products/products.html', content)
