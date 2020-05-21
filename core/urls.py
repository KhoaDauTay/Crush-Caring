from django.urls import path
from .views import (
    Home,
    ItemDetailView,
    CheckoutView,
    ShopView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    Appointment,
    Booking,
    booking_add,
    SearchResultsView
)


app_name = 'core'

urlpatterns = [
    path('', Home, name='home'),
    path('shoppage/', ShopView.as_view(), name='shoppage'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('booking/', Booking, name="booking"),
    path('bookingadd/<slug>/', booking_add, name='booking-add'),
    path('appointment', Appointment, name="appointment"),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
