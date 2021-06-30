from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Payment
from .forms import MakePaymentForm
from .services import charge_user
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

class PaymentListView(generic.ListView):
	model = Payment
	template_name = 'list_payments.html'

	

def make_payment(request):
	if request.method == 'POST':
		form = MakePaymentForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			amount = form.cleaned_data['amount']
			bank_code = form.cleaned_data['bank_code']
			account_number = form.cleaned_data['account_number']
			birthday = form.cleaned_data['birthday']
			pin = form.cleaned_data['pin']
			bank = {'account_number':account_number,'code':bank_code}
			response = charge_user(amount,email,bank,birthday)
			if response['gateway_response'] == 'Approved':
				new_payment = Payment.objects.create(reference= response['reference'],status=response['status'],email=response['email'])
				new_payment.save()
				return redirect('my_payments')
			if response['gateway_response'] == 'Pending':
				new_payment = Payment.objects.create(reference= response['reference'],status=response['status'],email=response['email'])
				new_payment.save()
				return redirect('my_payments')
			if response['gateway_response'] == "Declined":
				return redirect('failed_payment')

	if request.method == 'GET':
		form = MakePaymentForm()
		context = { 'form':form}
		return render(request,'make_payment.html',context)
