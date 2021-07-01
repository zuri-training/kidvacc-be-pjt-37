from django.urls import path
from .views import PaymentListAPIView, make_payment, verify_payment
from django.views.generic import TemplateView


urlpatterns = [
	path('my-payments/', PaymentListAPIView.as_view(),name='my_payments'),
	path('make-payment/',make_payment, name= 'make_payment' ),
	path('failed-payment/', TemplateView.as_view(template_name='failed_payment.html'), name='failed_payment'),
	path('verify-payment/<str:reference>', verify_payment, name='verify_payment')
]