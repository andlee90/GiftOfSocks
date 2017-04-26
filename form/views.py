from django.shortcuts import render, redirect
from django import forms
from .forms import OrderForm
from .models import *

def user_form(request):
	return render(request, 'user_form.html')

def admin_form(request):
	return render(request, 'admin_form.html')

#def user(request):
#	if request.method == "POST":
#		form = BuyerForm(request.POST)
#		if form.is_valid():
#			model_instance = form.save(commit=False)
#			model_instance.save()
#			return redirect('user.html')
#	else:
#		form = BuyerForm()
#	return render(request, "user.html", {'form':form})

#Working comprehensive table view/db interaction
#def user(request):
#	if request.POST:		
#		form = OrderTestForm(request.POST)
#		if form.is_valid():
#			form.save(commit=False)
#			form.save()
#			form = OrderTestForm()
#			return render(request, "user.html", {'form':form})
#	else:
#		form = OrderTestForm()
#	return render(request, "user.html", {'form':form})

#Testing saving data to other models for our DB design
def user(request):
	if request.POST:	
		form = OrderForm(request.POST)
		buyer = Buyer()
		buyerRole = BuyerRole()
		order = Order()
		buyerDelInfo = BuyerDeliveryInfo()
		if form.is_valid():
			data = form.cleaned_data
			if Buyer.objects.all().filter(email = data['email']).exists() == False:
				buyer.first_name = data['first_name']
				buyer.last_name = data['last_name']
				buyer.email = data['email']
				buyer.phone_number = data['phone_number']
				buyer.save()
				buyerRole.buyer_id = Buyer.objects.all().get(email = data['email'])
				buyerRole.role_id = Role.objects.all().get(role_id = data['role_id'])
				buyerRole.save()
				if data['delivery_id'] == 2:
					buyerDelInfo.buyer_id = Buyer.objects.all().get(email = data['email'])
					buyerDelInfo.building_name = data['building_name']
					buyerDelInfo.room_number = data['room_number']
					buyerDelInfo.save()
				order.buyer_id = Buyer.objects.all().get(email = data['email'])
				order.sock_id = Sock.objects.all().get(sock_id = data['sock_id'])
				order.charity_id = Charity.objects.all().get(charity_id = data['charity_id'])
				order.delivery_id = Delivery.objects.all().get(delivery_id = data['delivery_id'])
				order.save()
				form.save()
			else:
				existing_info = Buyer.objects.all().get(email = data['email'])
				if data['delivery_id'] == 2:
					buyerDelInfo.buyer_id = existing_info
					buyerDelInfo.building_name = data['building_name']
					buyerDelInfo.room_number = data['room_number']
					buyerDelInfo.save()
				order.buyer_id = existing_info
				order.sock_id = Sock.objects.all().get(sock_id = data['sock_id'])
				order.charity_id = Charity.objects.all().get(charity_id = data['charity_id'])
				order.delivery_id = Delivery.objects.all().get(delivery_id = data['delivery_id'])
				order.save()
				form.save()
			form = OrderForm()
			return render(request, "user.html", {'form':form})
	else:
		form = OrderForm()
	return render(request, "user.html", {'form':form})

def admin_shell(request):
	if request.method == 'POST' and 'total_socks' in request.POST:
		socks = Order.objects.count()
		return render(request, 'admin_shell.html', {'socks': socks})
	elif request.method == 'POST' and 'total_socks_charity' in request.POST:
		charities = Charity.objects.all()
		charities_list = charities.values_list("charity_name", flat=True)
		charity1_orders = Order.objects.filter(charity_id_id = 1).count()
		charity2_orders = Order.objects.filter(charity_id_id = 2).count()
		charity1 = charities_list[0]
		charity2 = charities_list[1]
		charity1 += ": " + str(charity1_orders)
		charity2 += ": " + str(charity2_orders)
		return render(request, 'admin_shell.html', {'charity1': charity1, 'charity2': charity2})
	elif request.method == 'POST' and 'total_socks_large' in request.POST:
		large_socks2 = Order.objects.filter(sock_id_id = 2).count()
		large_socks4 = Order.objects.filter(sock_id_id = 4).count()
		large_socks6 = Order.objects.filter(sock_id_id = 6).count()
		large_socks = large_socks2 + large_socks4 + large_socks6
		return render(request, 'admin_shell.html', {'large_socks': large_socks})
	


