<<<<<<< HEAD
=======
from django.db.models import fields
>>>>>>> e70e3fac976cc3bdc4c71f1d3b6437393e7635d0
from rest_framework import serializers
from .models import Payment
class GETPaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields= '__all__'

class POSTPaymentSerializer(serializers.Serializer):
	email = serializers.EmailField()
	amount = serializers.CharField()
	bank_code = serializers.CharField(max_length=3)
	account_number = serializers.CharField(max_length=17)
	birthday = serializers.CharField(max_length=10)
	pin = serializers.CharField(max_length=4)

<<<<<<< HEAD
=======
	class Meta:
		model = Payment
		fields= '__all__'
>>>>>>> e70e3fac976cc3bdc4c71f1d3b6437393e7635d0
class OTPSerializer(serializers.Serializer):
	otp = serializers.CharField()
	pin = serializers.CharField(max_length=4)