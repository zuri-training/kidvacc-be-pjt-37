#from rest_framework.views import APIView
from django.shortcuts import render
#from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Child, Parent, Hospital_Details, Hospital_Type, Appointment
from .serializers import ChildSerializer, ParentSerializer, Hospital_DetailsSerializer, Hospital_TypeSerializer, AppointmentSerializer
#from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.


class ListChild(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
class DetailChild(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ListParent(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class DetailParent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    

class ListHospital_Details(generics.ListCreateAPIView):
    queryset = Hospital_Details.objects.all()
    serializer_class = Hospital_DetailsSerializer

class DetailHospital_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital_Details.objects.all()
    serializer_class = Hospital_DetailsSerializer
    

class ListHospital_Type(generics.ListCreateAPIView):
     queryset = Hospital_Type.objects.all()
     serializer_class = Hospital_TypeSerializer

class DetailHospital_Type(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital_Type.objects.all()
    serializer_class = Hospital_TypeSerializer
    
class ListAppointment(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DetailAppointment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer  