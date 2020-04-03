from django.urls import path
from order_management.views import CompanyView, ProductView, CreateCompanyView, CreateProductView, PlaceOrderView, success

urlpatterns = [
    path('', CompanyView.as_view(), name='index'),
    path('products/', ProductView.as_view(), name='products'),
    path('createcompany/', CreateCompanyView.as_view(), name='create_company'),
    path('createproduct/', CreateProductView.as_view(), name='create_product'),
    path('placeorder/', PlaceOrderView.as_view(), name='place_order'),
    path('success/', success, name='success')
]
