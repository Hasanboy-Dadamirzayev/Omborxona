

from django.urls import path

from main.views import *



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mahsulotlar/', ProductsView.as_view(), name='products'),
    path('mahsulotlar/<int:product_id>/edit/', ProductUpdateView.as_view(), name='edit'),
    path('mahsulotlar/<int:product_id>/delete/', ProdcutDeleteView.as_view(), name='delete'),
    path('mijozlar/', CustomersView.as_view(), name='customers')
]