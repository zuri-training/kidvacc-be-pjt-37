from django import forms

class MakePaymentForm(forms.Form):
	email = forms.EmailField()
	amount = forms.CharField()
	bank_code = forms.CharField(max_length=3, help_text="Your 3 digit bank code")
	account_number = forms.CharField(max_length=10)
	birthday = forms.CharField() 

	pin = forms.CharField(required=False)
	
