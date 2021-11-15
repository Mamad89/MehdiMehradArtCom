from django.shortcuts import render
from .forms import ContactForm


# Create your views here.

def main_index(request):
	return render(request, 'app_main/index.html')


def main_about(request):
	return render(request, 'app_main/about.html')


def main_contact_us(request):
	contact_us_form = ContactForm(request.POST or None)
	content = {
		"form": contact_us_form
	}
	return render(request, 'app_main/contact_us.html', content)
