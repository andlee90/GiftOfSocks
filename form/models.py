from django.db import models

class Buyer(models.Model):
	buyer_id = models.AutoField('buyer')
	buyer_id.primary_key = True
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	areacode = models.IntegerField(max_length=3)
	exchange = models.IntegerField(max_length=3)
	extension = models.IntegerField(max_length=4)

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

class BuyerRole(models.Model):
	buyer_id = models.ForeignKey('buyer')
	role_id = models.ForeignKey('role')

class Order(models.Model):
	order_id = models.AutoField('order')
	order_id.primary_key = True
	buyer_id = models.ForeignKey('buyer')
	sock_id = models.ForeignKey('Sock')
	charity_id = models.ForeignKey('charity')
	delivery_id = models.ForeignKey('delivery')
	
class BuyerDeliveryInfo(models.Model):
	buyer_id = models.ForeignKey('buyer')
	building_name = models.CharField(max_length=30)
	room_number = models.CharField(max_length=10)


class Meta:
	db_table=u'Buyer'

	def __unicode__(self):
		return u"%d %s %s %s %d" % (self.pk, self.first_name, self.last_name, self.email,self.phone)

