from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_page, name='q21_checkout'),
    path('create-checkout-session/', views.create_checkout_session, name='q21_create_checkout_session'),
    path('success/', views.payment_success, name='q21_payment_success'),
    path('cancel/', views.payment_cancel, name='q21_payment_cancel'),
]
