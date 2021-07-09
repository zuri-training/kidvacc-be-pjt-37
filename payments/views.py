from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .models import Payment
from .serializers import GETPaymentSerializer,POSTPaymentSerializer, OTPSerializer
from .services import paystack_charge
from django.forms.models import model_to_dict
import json
from django.contrib.auth.models import BaseUserManager
# Create your views here.

class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = GETPaymentSerializer

    
@api_view(['POST'])
def make_payment(request):
    if request.method == 'POST':
        serializer = POSTPaymentSerializer(data=request.data)
        if serializer.is_valid():

            email = serializer.validated_data['email']
            amount = serializer.validated_data['amount']
            bank_code = serializer.validated_data['bank_code']
            account_number = serializer.validated_data['account_number']
            birthday = serializer.validated_data['birthday']
            pin = serializer.validated_data['pin']
            bank = {'account_number':account_number,'code':bank_code}
            
            response = paystack_charge.start_charge( email=email,amount=amount, bank={"account_number":account_number,"code":bank_code},birthday=birthday)
            
            if response['status'] == True:
                reference = response['data']['reference']
                return Response({"status":"True","reference":f"{reference}"}, status=status.HTTP_302_FOUND)
            if response['status'] == False:
                print('Failed Payment')
                return Response({"status":"False", "message":f"{response['message']}"}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({"status":"False"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])    
def verify_payment(request, reference):
    if request.method == 'POST':
        serializer  = OTPSerializer(data = request.data)
        if serializer.is_valid():
            pin = serializer['pin']
            otp = serializer['otp']
            response3 = paystack_charge.submit_otp(otp=otp,reference=reference)
            response2 = paystack_charge.submit_pin(pin =pin,reference=reference)
            
            response5 = paystack_charge.check_pending(reference=reference)
            if response5['status'] == True and response5['data']['gateway_response'] == 'Approved':
                new_payment = Payment.objects.create(reference= reference,status=response5['status'],email=response5['data']['customer']['email'])
                new_payment.save()
                return Response({"status":True}, status=status.HTTP_302_FOUND)

            if response5['status'] == False:
                return JsonResponse({"status":"False","message":f"{response5['message']}"}, status=status.HTTP_400_BAD_REQUEST)
           
            return Response({"status":"False", "message":"Unknown error occured"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        payments = Payment.objects.filter(reference=reference)
        serializer = GETPaymentSerializer(payments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
