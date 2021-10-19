from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JmHaRBRcXv1stNj9XnasjRGW5y1C1hzHNeC2EWTmVqARc7aDGWK5KPqQBPg4TCb1UXfo4JVAGHeDphICCanuPaj00np3QN2x8',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)


