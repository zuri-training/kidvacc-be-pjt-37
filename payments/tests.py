from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APITestCase
from .models import Payment
from django.utils import timezone 
from uuid import uuid4
from .models import Payment
import json
from rest_framework import status
# Create your tests here.

class PaymentsTests(APITestCase):

	def setUp(self):
		self.factory = APIRequestFactory()
	
	def test_payment_model(self):
		new_payment = Payment.objects.create(reference="",
												status='success',
												paid_at=timezone.now(),
												email="test@user.com",)
		count = Payment.objects.count()

		self.assertEqual(1,count)

	def test_make_payment_api(self):
		request = self.client.post('/payments/make-payment/', {"email":"test@user.com","amount":"456",
									"bank_code":"057",
									"account_number":"0000000000",
									"birthday":"1995-09-23",
									"pin":"0000"})
		self.assertEqual(request.status_code,status.HTTP_302_FOUND)
		self.refernce = request.data['reference']
	def test_verify_payment_api(self):
		request = self.client.post(f'/payments/verify-payment/{self.reference}/',{"otp":"123456","pin":"0000"})
		
		self.assertEqual(request.status_code,status.HTTP_302_FOUND)
