from django import forms

from .models import Buyer
from .models import OrderTest
from .models import Sock

class BuyerForm(forms.ModelForm):

    class Meta:

        model = Buyer
        fields = ('first_name', 'last_name', 'email', 'areacode','exchange','extension')

# Test class for Demo. Should delete once table is dropped
class OrderTestForm(forms.ModelForm):

	#sock_id = forms.TypedChoiceField(choices = sock_types, widget = forms.RadioSelect())
	sock_id = forms.ModelChoiceField(queryset = Sock.objects, widget = forms.RadioSelect(), empty_label=None)
	
	class Meta:

		model = OrderTest
		fields = ('sock_id',)

# Ideas for applying labels to the listed radio buttons
class socksForm(forms.ModelForm):
    choices = (
        (1, 'ESU Colors - Medium - Men (6-8) Donation $20'),
        (2, 'ESU Colors - Large - Men (9-13) Donation $20'), 
        (3, 'Neon Colors - Medium - Men (6-8) Donation $20'), 
        (4, 'Neon Colors - Large - Men (9-13) Donation $20'), 
        (5, 'ESU Colors - Medium - Women (6-9) Donation $20'), 
        (6, 'ESU Colors - Large - Women (10-13) Donation $20'),
        (7, 'Neon Colors - Medium - Women (6-9) Donation $20'), 
        (8, 'Neon Colors - Large - Women (10-13) Donation $20')
    )
    sock_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
    class Meta:

		model = OrderTest
		fields = ('sock_choices',)