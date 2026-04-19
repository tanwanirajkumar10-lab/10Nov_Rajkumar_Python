from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('pay/<int:appointment_id>/', views.initiate_payment, name='initiate_payment'),
    path('mock-checkout/', views.mock_checkout, name='mock_checkout'),
    path('callback/', views.payment_callback, name='payment_callback'),
]
