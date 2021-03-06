import sys, os

from django.shortcuts import render, redirect, HttpResponseRedirect
from django import forms
from .forms import OrderForm
from .models import *

#User form
def user(request):
	if request.method == 'POST' and 'submit' in request.POST:	
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
			#Prevent duplicate data submission
			return HttpResponseRedirect('/user/')
	else:
		form = OrderForm()
	return render(request, "user.html", {'form':form})

#Admin form
def admin_shell(request):

	#Handles searching for a user by email address
	if request.method == 'POST' and 'find_user_button' in request.POST:
		
		user_input = request.POST.get('find_user', None)
		user_data = Comprehensive.objects.filter(email=user_input)
		firstname = user_data.values_list("first_name", flat=True)
		lastname = user_data.values_list("last_name", flat=True)
		email = user_data.values_list("email", flat=True)
		phone = user_data.values_list("phone_number", flat=True)

		sock_id = user_data.values_list("sock_id", flat=True)
		sock_obj = Sock.objects.filter(sock_id = sock_id)
		sock = sock_obj.values_list("sock_type", flat=True)

		charity_id = user_data.values_list("charity_id", flat=True)
		charity_obj = Charity.objects.filter(charity_id = charity_id)
		charity = charity_obj.values_list("charity_name", flat=True)

		role_id = user_data.values_list("role_id", flat=True)
		role_obj = Role.objects.filter(role_id = role_id)
		role = role_obj.values_list("role_name", flat=True)

		delivery_id = user_data.values_list("delivery_id", flat=True)
		delivery_obj = Delivery.objects.filter(delivery_id = delivery_id)
		delivery = delivery_obj.values_list("delivery_option", flat=True)

		building = user_data.values_list("building_name", flat=True)
		room = user_data.values_list("room_number", flat=True)

		info = [("First Name: " + str(firstname[0])), 
			("Last Name: " + str(lastname[0])),
			("First Name: " + str(email[0])), 
			("Phone Number: " + str(phone[0])),
			("Sock Choice: " + str(sock[0])), 
			("Charity Choice: " + str(charity[0])), 
			("Role Choice: " + str(role[0])), 
			("Delivery Choice: " + str(delivery[0])),  
			("Building: " + str(building[0])),
			("Room #: " + str(room[0]))]

		return render(request, "admin_user_results.html", {'info':info}) 

	#Handles adding a new charity
	if request.method == 'POST' and 'add_charity_button' in request.POST:
		
		user_input = request.POST.get('add_charity', None)
		new_charity = Charity()
		new_charity.charity_name = user_input
		new_charity.save()
		info_raw = Charity.objects.filter(charity_name = user_input)
		info = info_raw.values_list("charity_name", flat=True)

		#Refresh Server
		os.system("touch ~/GiftOfSocks/GiftOfSocks/wsgi.py")

		return render(request, "admin_new_charity.html", {'info':info[0]})
	
	#Handles recovering data for all button-only based queries
	if request.method == 'GET':

		#Get total socks
		socks = Order.objects.count()

		#Get total socks by charity
		charities = Charity.objects.all()
		charity_size = Charity.objects.all().count()
		charities_raw = charities.values_list("charity_name", flat=True)
		charities_list = []

		for i in range(0,charity_size):
			charity = charities_raw[i]
			charity_ids = Charity.objects.filter(charity_name = charity)
			charity_id_list = charity_ids.values_list("charity_id", flat=True)
			charity_orders = Order.objects.filter(charity_id_id = charity_id_list[0]).count()
			charity += ": " + str(charity_orders)
			charities_list.append(charity)

		#Get total large socks
		large_socks2 = Order.objects.filter(sock_id_id = 2).count()
		large_socks4 = Order.objects.filter(sock_id_id = 4).count()
		large_socks6 = Order.objects.filter(sock_id_id = 6).count()
		large_socks = large_socks2 + large_socks4 + large_socks6

		#Get list of orders to be delivered
		deliveries = Comprehensive.objects.filter(delivery_id = 2)
		size = Comprehensive.objects.filter(delivery_id = 2).count()
		firstname_list = deliveries.values_list("first_name", flat=True)
		lastname_list = deliveries.values_list("last_name", flat=True)
		sock_list = deliveries.values_list("sock_id", flat=True)
		building_list = deliveries.values_list("building_name", flat=True)
		room_list = deliveries.values_list("room_number", flat=True)
		deliveries_list = []
		for i in range(0,size):
			firstname = firstname_list[i]
			lastname = lastname_list[i]
			sock_id = sock_list[i]
			sock_obj = Sock.objects.filter(sock_id = sock_id)
			sock_type = sock_obj.values_list("sock_type", flat=True)
			sock = sock_type[0]
			building = building_list[i]
			room = room_list[i]
			result = str(firstname) + " " + str(lastname) + ", " + str(sock) + ", " + str(building) + ",  " + str(room)
			deliveries_list.append(result)

		return render(request, 'admin_shell.html', 
			{'socks':socks, 
			'charities_list':charities_list, 
			'large_socks':large_socks, 
			'deliveries_list':deliveries_list})

#Page for displaying a user's form submission
def admin_user_results(request):
	return render(request, "admin_user_results.html", {})

#Page for displaying the name of the charity that was added
def admin_new_charity(request):
	return render(request, "admin_new_charity.html", {})

	
	


