from django.db import models
from GiftOfSocks.choices import *
from django.core.validators import RegexValidator

class Sock(models.Model):
	sock_id = models.AutoField('sock')
	sock_id.primary_key = True
	sock_type = models.CharField(max_length=30)

class Charity(models.Model):
	charity_id = models.AutoField('charity')
	charity_id.primary_key = True
	charity_name = models.CharField(max_length=30)

class Role(models.Model):
	role_id = models.AutoField('role')
	role_id.primary_key = True
	role_name = models.CharField(max_length=30)

class Delivery(models.Model):
	delivery_id = models.AutoField('delivery')
	delivery_id.primary_key = True
	delivery_option = models.CharField(max_length=30)

class Buyer(models.Model):
	buyer_id = models.AutoField('buyer')
	buyer_id.primary_key = True
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{10,10}$', message="Phone number must be entered in the format: '+999999999'. 10 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=10)

class BuyerRole(models.Model):
	buyer_id = models.ForeignKey('buyer')
	role_id = models.ForeignKey('role')

class BuyerDeliveryInfo(models.Model):
	buyer_id = models.ForeignKey('buyer')
	building_name = models.CharField(max_length=30)
	room_number = models.CharField(max_length=10)

class Order(models.Model):
	order_id = models.AutoField('order')
	order_id.primary_key = True
	buyer_id = models.ForeignKey('buyer')
	sock_id = models.ForeignKey('sock')
	charity_id = models.ForeignKey('charity')
	delivery_id = models.ForeignKey('delivery')

def get_charity_choices():
	if Charity.objects.all().exists() == True:
		charity_choices = Charity.objects.values_list('charity_id', 'charity_name')
	else:
		charity_choices = choices3
	return charity_choices

class Comprehensive(models.Model):
	order_id = models.AutoField('Order')
	order_id.primary_key = True
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{10,10}$', message="Phone number must be entered in the format: '+999999999'. 10 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=10) # validators should be a list
	sock_id = models.IntegerField(choices= choices, default=0, verbose_name='Sock Choice')
	charity_id = models.IntegerField(choices= get_charity_choices() , default=0, verbose_name='Charity')
	role_id = models.IntegerField(choices= choices2, default=0, verbose_name='Role')
	delivery_id = models.IntegerField(choices= choices4, default=0, verbose_name='Delivery Option')
	building_name = models.CharField(max_length=30,null=True, blank=True)
	room_number = models.CharField(max_length=3,null=True, blank=True)

