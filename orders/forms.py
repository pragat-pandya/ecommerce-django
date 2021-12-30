from django import forms
from .models import Order

class OrderForm (forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'addres_line_1', 'addres_line_2', 'country', 'city', 'order_note']
