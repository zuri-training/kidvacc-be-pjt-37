from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Child, Parent, Hospital_Details, Hospital_Type, Appointment
from .serializers import ChildSerializer, ParentSerializer, Hospital_DetailsSerializer, Hospital_TypeSerializer, AppointmentSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.


class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    
    

class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    

class Hospital_DetailsList(generics.ListCreateAPIView):
    queryset = Hospital_Details.objects.all()
    serializer_class = Hospital_DetailsSerializer

class Hospital_DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital_Details.objects.all()
    serializer_class = Hospital_DetailsSerializer
    


class Hospital_TypeList(generics.ListCreateAPIView):
     queryset = Hospital_Type.objects.all()
     serializer_class = Hospital_TypeSerializer

class Hospital_TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital_Type.objects.all()
    serializer_class = Hospital_TypeSerializer
    


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    