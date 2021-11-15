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
