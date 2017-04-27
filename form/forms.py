from django import forms
from GiftOfSocks.choices import *
from .models import Comprehensive

# Form for user interactions
class OrderForm(forms.ModelForm):

	class Meta:

		model = Comprehensive
		fields = ('first_name', 'last_name', 'email', 'phone_number','sock_id','charity_id','role_id','delivery_id','building_name','room_number',)

