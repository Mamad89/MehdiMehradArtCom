from django.urls import path
from . import views

urlpatterns = [
	path('', views.main_index, name='index'),
	path('about-us', views.main_about, name='about-us'),
	path('contact_us', views.main_contact_us, name='contact-us'),
	path('login', views.main_login, name='login'),
	path('register', views.main_register, name='register'),
]
