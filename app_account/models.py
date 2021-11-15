from django.db import models


# Create your models here.


class Account(models.Model):
	email = models.CharField(max_length=100, null=True)
	password = models.CharField(max_length=100, null=True)


class User(models.Model):
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	gender = models.BooleanField(null=True)
	phone = models.CharField(max_length=11, null=True)
	address = models.TextField(null=True)
	account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
