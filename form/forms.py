from django import forms

from .models import Buyer
from .models import OrderTest
from .models import Sock

# Not currently being used.
sock_types = ((1, 'ESU Colors - Medium - Men (6-8) Donation $20'),
        (2, 'ESU Colors - Large - Men (9-13) Donation $20'), 
        (3, 'Neon Colors - Medium - Men (6-8) Donation $20'), 
        (4, 'Neon Colors - Large - Men (9-13) Donation $20'), 
        (5, 'ESU Colors - Medium - Women (6-9) Donation $20'), 
        (6, 'ESU Colors - Large - Women (10-13) Donation $20'),
        (7, 'Neon Colors - Medium - Women (6-9) Donation $20'), 
        (8, 'Neon Colors - Large - Women (10-13) Donation $20'))

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
class MyForm(forms.Form):
    MY_CHOICES = (
        ('opt0', 'Option zero'),
        ('opt1', 'Option one'),
    )
    myfield = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES)

    def myfield_choices(self):
        """
        Returns myfield's widget's default renderer, which can be used to 
            render the choices of a RadioSelect widget.
        """
        field = self['myfield']
        widget = field.field.widget

        attrs = {}
        auto_id = field.auto_id
        if auto_id and 'id' not in widget.attrs:
            attrs['id'] = auto_id

        name = field.html_name

        return widget.get_renderer(name, field.value(), attrs=attrs)

