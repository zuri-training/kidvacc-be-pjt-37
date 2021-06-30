from django.urls import path
from .views import PaymentListView, make_payment
from django.views.generic import TemplateView


urlpatterns = [
	path('my-payments/', PaymentListView.as_view(),name='my_payments'),
	path('make-payment/',make_payment, name= 'make_payment' ),
	path('failed-payment/', TemplateView.as_view(template_name='failed_payment.html'))
]