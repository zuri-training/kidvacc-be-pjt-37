from django import forms

class MakePaymentForm(forms.Form):
	email = forms.EmailField()
	amount = forms.CharField()
	bank_code = forms.CharField(max_length=3, help_text="Your 3 digit bank code")
	account_number = forms.CharField(max_length=10)
	birthday = forms.CharField() 
	pin = forms.CharField()
	
class RequestPinForm(forms.Form):
	pass

class RequestOTPForm(forms.Form):
	otp =  forms.CharField()
	pin = forms.CharField(max_length=4)

class RequestBirthdayForm(forms.Form):
	birthday = forms.CharField()

