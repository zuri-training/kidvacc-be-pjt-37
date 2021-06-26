from django.urls import path
from .views import ListChild, DetailChild, ListParent, DetailParent, ListHospital_Type, DetailHospital_Type, ListHospital_Details, DetailHospital_Details, ListAppointment, DetailAppointment
                    
urlpatterns = [
    path('child/', ListChild.as_view(), name="child"),
    path('child/<int:pk>/', DetailChild.as_view(), name='detail-child'),
    path('parent', ListParent.as_view(), name='parent'),
    path('parent/<int:pk>/', DetailParent.as_view(), name='detail-parent'),
    path('hospital_type', ListHospital_Type.as_view(), name='hospital-type'),
    path('hospital_type/<int:pk>/', DetailHospital_Type.as_view(), name='detail-hospital_type'),

    path('hospital_details', ListHospital_Details.as_view(), name='hospital_details'),
    path('hospital_details/<int:pk/', DetailHospital_Details.as_view(), name='detail-hospital_details'),
    path('appointment', ListAppointment.as_view(), name='appointment'),
    path('appointment/<int:pk/', DetailAppointment.as_view(), name='detail-appointment')
]
