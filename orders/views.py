from django.shortcuts import render
from carts.models import CartItem
from django.http import HttpResponse
# Create your views here.

def place_order (request):
    return HttpResponse('place_order view ')
    #current_user = request.user
    #cart_items = CartItem.objects.filter(user=current_user)
    #cart_count = cart_items.count()
    #if cart_count < 0:
#        return redirect('store')

#    if request.mehtod == 'POST':
#        form = OrderForm(request.POST)
