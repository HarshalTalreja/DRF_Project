from django.shortcuts import render
from order_management import models
from django.views.generic import ListView, CreateView


# Create your views here.
def success(request):
    return render(request, 'order_management/invoice.html')

class CompanyView(ListView):
    model = models.Company

class ProductView(ListView):
    model = models.Product

class CreateCompanyView(CreateView):
    fields = ('Name', 'GST_NO')
    model = models.Company

class CreateProductView(CreateView):
    fields = ('Name', 'Company', 'Cost')
    model = models.Product

class PlaceOrderView(CreateView):
    fields = ('Order_No', 'Company', 'Product', 'Rate', 'Quantity', 'Total_Price')
    model = models.Purchase
