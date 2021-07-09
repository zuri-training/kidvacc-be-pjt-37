from django.db.models import fields
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

	class Meta:
		model = Payment
		fields= '__all__'
class OTPSerializer(serializers.Serializer):
	otp = serializers.CharField()
	pin = serializers.CharField(max_length=4)