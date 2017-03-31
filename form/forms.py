from django import forms
from GiftOfSocks.choices import *

from .models import Buyer
from .models import OrderTest
from .models import Sock
from .models import Comprehensive
from .models import BuyerDeliveryInfo


class BuyerForm(forms.ModelForm):

    class Meta:

        model = Buyer
        fields = ('first_name', 'last_name', 'email', 'areacode','exchange','extension')

# Ideas for applying labels to the listed radio buttons
class socksForm(forms.ModelForm):
    sock_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
    class Meta:

		model = OrderTest
		fields = ('sock_choices',)

class rolesForm(forms.ModelForm):
    role_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices2)
    class Meta:

		model = OrderTest
		fields = ('role_choices',)

class charityForm(forms.ModelForm):
    charity_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices3)
    class Meta:

		model = OrderTest
		fields = ('charity_choices',)

class delOptForm(forms.ModelForm):
    delOpt_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices4)
    class Meta:

		model = OrderTest
		fields = ('delOpt_choices',)

class delInfoForm(forms.ModelForm):

    class Meta:

        model = BuyerDeliveryInfo
        fields = ('building_name', 'room_number',)

# Test class for Demo. Should delete once table is dropped
class OrderTestForm(forms.ModelForm):
	#radio button declarations for comprehensive table

	sock_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
	role_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices2)
	charity_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices3)
	delOpt_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices4)
	class Meta:

		model = Comprehensive
		fields = ('first_name', 'last_name', 'email', 'areacode','exchange','extension','sock_choices','charity_choices','role_choices','delOpt_choices','building_name','room_number',)
