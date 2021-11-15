from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_products_page, name='products'),
]
