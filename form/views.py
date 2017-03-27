from django.shortcuts import render, redirect
from django import forms
from .forms import OrderTestForm
from .models import Sock
from .models import OrderTest

def user_form(request):
	return render(request, 'user_form.html')

def admin_form(request):
	return render(request, 'admin_form.html')

#def user(request):
#	if request.method == "POST":
#		form = OrderTestForm(request.POST)
#		if form.is_valid():
#			model_instance = sock.save(commit=False)
#			model_instance.save()
#			return redirect('user_form.html')
#	else:
#		form = OrderTestForm()
#	return render(request, "user.html", {'form':form})

# Test view for demo
def user(request):
	if request.method == "POST":
		#sock = Sock(request.POST['sock_id'])
		form = OrderTestForm(request.POST)
		#form.sock_id = sock
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('user_form.html')
	else:
		form = OrderTestForm()
	return render(request, "user.html", {'form':form})

# Test view for demo
def admin_query(request):
	socks = OrderTest.objects.count()
	return render(request, 'admin_query.html', {'socks': socks})

# Test view for demo
def admin_test(request):
	return render(request, 'admin_query.html')
