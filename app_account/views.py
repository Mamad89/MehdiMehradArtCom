from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


# Create your views here.


def main_login(request):
	login_form = LoginForm(request.POST or None)
	context = {
		"form": login_form
	}
	if login_form.is_valid():
		context["form"] = LoginForm()
		userName = login_form.cleaned_data.get("userName")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request, username=userName, password=password)
		if user is not None:
			login(request, user)
			context["form"] = LoginForm()
			return redirect('/')

		else:
			print('Error')

	return render(request, '../../app_account/templates/app_account/login.html', context)


User = get_user_model()


def main_register(request):
	register_form = RegisterForm(request.POST or None)
	context = {
		"form": register_form
	}
	if register_form.is_valid():
		context["form"] = RegisterForm()
		userName = register_form.cleaned_data.get("userName")
		email = register_form.cleaned_data.get("email")
		password = register_form.cleaned_data.get("password")
		User.objects.create_user(username=userName, email=email, password=password)
	return render(request, '../../app_account/templates/app_account/Register.html', context)
