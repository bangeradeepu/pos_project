from rest_framework import serializers
from .models import Customers, CustomerAddresses

class CustomerAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddresses
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    addresses = CustomerAddressesSerializer(many=True, read_only=True)

    class Meta:
        model = Customers
        fields = '__all__'
