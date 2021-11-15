from django.db import models


# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField(null=True)
	short_distribution = models.CharField(max_length=300)
	distribution = models.TextField(null=True)
	is_exist = models.BooleanField(null=True)
	pic = models.ImageField(null=True, verbose_name='image')
