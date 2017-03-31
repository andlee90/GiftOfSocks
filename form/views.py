from django.shortcuts import render, redirect
from django import forms

from .forms import OrderTestForm
from .forms import socksForm
from .forms import BuyerForm

from .models import Sock
from .models import OrderTest
from .models import Comprehensive

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

#Testing comprehensive table view/db interaction
def user(request):
	if request.POST:		
		form = OrderTestForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.save()
			form = OrderTestForm()
			return render(request, "user.html", {'form':form})
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
