from rest_framework import generics
from order_management.models import Company, Product, Purchase
from order_management.api.serializers import ComapanyAPISerializer, ProductAPISerializer, PurchaseAPISerializer


# Create your views here.

class CompanyAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = ComapanyAPISerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAPISerializer


class PurchaseAPIView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseAPISerializer
