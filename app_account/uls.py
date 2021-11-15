from django.urls import path
from . import views

urlpatterns = [
	path('login', views.main_login, name='login'),
	path('register', views.main_register, name='register'),
]
