from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
	full_name = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={"class": "form-control my-3", "placeholder": "Full name ..."}))
	Phone = forms.CharField(
		label='',
		widget=forms.NumberInput(attrs={"class": "form-control my-3", "placeholder": "Phone number ..."}))
	Massage = forms.CharField(
		label='',
		widget=forms.Textarea(attrs={"class": "form-control my-3", "placeholder": "Address ..."}))
	email = forms.EmailField(
		label='',
		widget=forms.EmailInput(attrs={"class": "form-control my-3", "placeholder": "Email ..."}))


class LoginForm(forms.Form):
	userName = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={"class": "form-control my-3", "placeholder": "User name ..."}))
	password = forms.CharField(
		label='',
		widget=forms.PasswordInput(attrs={"class": "form-control my-3", "placeholder": "Password ..."}))


class RegisterForm(forms.Form):
	userName = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={"class": "form-control my-3", "placeholder": "User name ..."}))
	email = forms.EmailField(
		label='',
		widget=forms.EmailInput(attrs={"class": "form-control my-3", "placeholder": "Email ..."}))
	password = forms.CharField(
		label='',
		widget=forms.PasswordInput(attrs={"class": "form-control my-3", "placeholder": "Password ..."}))
	password2 = forms.CharField(
		label='',
		widget=forms.PasswordInput(attrs={"class": "form-control my-3", "placeholder": "Password again ..."}))

	def clean_userName(self):
		userName = self.cleaned_data.get("userName")
		qs = User.objects.filter(username=userName)
		if qs.exists():
			raise forms.ValidationError("user name is taken")
		return userName

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")

		if password != password2:
			raise forms.ValidationError("Passwords must match")
		return data
