from django.shortcuts import render
from carts.models import CartItem
# Create your views here.

def place_order (request):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count < 0:
        return redirect('store')

    if request.mehtod == 'POST':
        form = OrderForm(request.POST)
