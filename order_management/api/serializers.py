from rest_framework.serializers import ModelSerializer
from order_management import models

class ComapanyAPISerializer(ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class ProductAPISerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class PurchaseAPISerializer(ModelSerializer):
    class Meta:
        model = models.Purchase
        exclude = ('Order_No',)
