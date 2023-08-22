from rest_framework import serializers
from pos_project import constants

class AddressGetValidation(serializers.Serializer):
    customer_id = serializers.IntegerField(required=False)
    count = serializers.IntegerField(required=False)
    offset = serializers.IntegerField(required=False)

class PostCustomerAddressValidation(serializers.Serializer):
    customer_id = serializers.IntegerField()
    address = serializers.CharField(min_length=10)
    locality = serializers.CharField(min_length=2)
    coordinates = serializers.DictField(
        child=serializers.DecimalField(min_value=3, max_digits=20, decimal_places=10)
    )
    type = serializers.ChoiceField(choices=list(constants.ADDRESS_TYPES.keys()))
    other_tag = serializers.CharField(min_length=3, required=False)

class PutCustomerAddressValidation(serializers.Serializer):
    customer_id = serializers.IntegerField()
    id = serializers.IntegerField()
    address = serializers.CharField(min_length=10, required=False)
    locality = serializers.CharField(min_length=2, required=False)
    coordinates = serializers.DictField(
        child=serializers.DecimalField(min_value=3, max_digits=20, decimal_places=10)
    )
    type = serializers.ChoiceField(choices=list(constants.ADDRESS_TYPES.keys()))
    other_tag = serializers.CharField(min_length=3, required=False)

class DeleteCustomerAddressValidation(serializers.Serializer):
    customer_id = serializers.IntegerField()
    id = serializers.IntegerField()

class PostValidation(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField(min_length=10)
    alt_phone = serializers.CharField(min_length=10, required=False)
    photo = serializers.CharField(required=False)
    email = serializers.EmailField()

class PutValidation(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    phone = serializers.CharField(min_length=10, required=False)
    alt_phone = serializers.CharField(min_length=10, required=False)
    photo = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    login_status = serializers.BooleanField(required=False)

class DeleteValidator(serializers.Serializer):
    id = serializers.IntegerField()