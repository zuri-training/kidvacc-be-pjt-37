from django.urls import path
from .views import ChildList, ChildDetail, ParentList, ParentDetail, Hospital_TypeList, Hospital_TypeDetail, Hospital_DetailsList, Hospital_DetailsDetail, AppointmentList, AppointmentDetail

urlpatterns = [

    
    path('child/', ChildList.as_view(), name="child"), 
    path('child/<int:pk>/', ChildDetail.as_view(), name='detail-child'),
    path('parent', ParentList.as_view(), name="parent"),
    path('parent/<int:pk>/', ParentDetail.as_view(), name='detail-parent'),
    path('hospital_type/', Hospital_TypeList.as_view(), name='hospital-type'), 
    path('hospital_type/<int:pk>/', Hospital_TypeDetail.as_view(), name='detail-hospital_type'),
    path('hospital_details/', Hospital_DetailsList.as_view(), name='hospital_details'),
    path('hospital_details/<int:pk>/', Hospital_DetailsDetail.as_view(), name='detail-hospital_details'),
    path('appointment/', AppointmentList.as_view(), name='appointment'),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name='detail-appointment')
]