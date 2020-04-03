from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    Name = models.CharField(max_length=256)
    GST_NO = models.CharField(max_length=256)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('index')


class Product(models.Model):
    Name = models.CharField(max_length=256, unique=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Cost = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('products')

class Purchase(models.Model):
    Order_No = models.CharField(max_length=256)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Rate =  models.IntegerField()
    Quantity = models.IntegerField()
    Total_Price = models.IntegerField()

    def __str__(self):
        return self.Order_No

    def get_absolute_url(self):
        return reverse('success')
