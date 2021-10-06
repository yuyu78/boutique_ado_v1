from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jhd8RBWfcC3iv59lgWJMphNlzBhLTrIkoLIs8NP4qbDtfMiZV1hHpO8JV4ItiF9IokUrnFCyAEJxTJw7C0loxAN00U9PZJxh6',
        'client_secret': 'text client secret', 
    }

    return render(request, template, context)