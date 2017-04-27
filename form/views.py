from django.shortcuts import render, redirect
from django import forms
from .forms import OrderForm
from .models import *

def user_form(request):
	return render(request, 'user_form.html')

def admin_form(request):
	return render(request, 'admin_form.html')

#Working user form
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
	
	if request.method == 'GET':

		#Get total socks
		socks = Order.objects.count()

		#Get total socks by charity
		charities = Charity.objects.all()
		charities_list = charities.values_list("charity_name", flat=True)
		charity1_orders = Order.objects.filter(charity_id_id = 1).count()
		charity2_orders = Order.objects.filter(charity_id_id = 2).count()
		charity1 = charities_list[0]
		charity2 = charities_list[1]
		charity1 += ": " + str(charity1_orders)
		charity2 += ": " + str(charity2_orders)

		#Get total large socks
		large_socks2 = Order.objects.filter(sock_id_id = 2).count()
		large_socks4 = Order.objects.filter(sock_id_id = 4).count()
		large_socks6 = Order.objects.filter(sock_id_id = 6).count()
		large_socks = large_socks2 + large_socks4 + large_socks6

		#Get list of orders to be delivered
		deliveries = Comprehensive.objects.filter(delivery_id = 1)
		size = Comprehensive.objects.filter(delivery_id = 1).count()
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

		#Get user info by email address

		#Add new charity
		return render(request, 'admin_shell.html', 
			{'socks':socks, 
			'charity1':charity1, 
			'charity2':charity2, 
			'large_socks':large_socks, 
			'deliveries_list':deliveries_list})

def admin_user_results(request):
	return render(request, "admin_user_results.html", {})

	
	


