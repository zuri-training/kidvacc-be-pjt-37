
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import generics, permissions
from .models import Child, Parent, Hospital_Details, Hospital_Type, Appointment
from .permissions import IsAuthorOrReadOnly 
from .serializers import ChildSerializer, ParentSerializer, Hospital_DetailsSerializer, Hospital_TypeSerializer, AppointmentSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView


# Create your views here
class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class Hospital_DetailsList(generics.ListCreateAPIView):
    queryset = Hospital_Details.objects.all()
    serializer_class = Hospital_DetailsSerializer


class Hospital_DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
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

class AppointmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def perform_create(self,serializer):
        user = self.request.user
        try:
            serializer.save(parent=user)
        except IntegrityError:
            return Response({"detail":"An error occured, please try again."},status=status.HTTP_400_BAD_REQUEST)
    
    # def perform_create(self, serializer):
    #     appointment = get_object_or_404(Appointment, pk=self.kwargs['pk'])
    #     serializer.save(parent=self.request.parent, appointment=appointment)
