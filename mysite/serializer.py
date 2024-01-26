from rest_framework import serializers
from .models import Customers
from .models import products,cart

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model=Customers
        fields ='__all__'

        
class productsSerializer(serializers.ModelSerializer):

    class Meta:
        model=products
        fields ='__all__'


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model=cart
        fields ='__all__'