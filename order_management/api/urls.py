from django.urls import path
from order_management.api.views import CompanyAPIView, ProductAPIView, PurchaseAPIView

urlpatterns = [
    path('companies/', CompanyAPIView.as_view(), name='index_api'),
    path('products', ProductAPIView.as_view(), name='products_api'),
    path('purchase/', PurchaseAPIView.as_view(), name='orders_api'),
]
