from django import forms
from rest_framework import serializers
from pos_project import constants
from customers.models import Customers
from menu.models import  Items 
from menu.categories.models import Categories
from .models import CouponCodes,CustomerCuponUsage,InfluencerCouponCodes
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.fields import IntegerField, BooleanField

class CouponPostSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3)
    description = serializers.CharField(min_length=6)
    coupon_type = serializers.ChoiceField(choices=[(key, key) for key in constants.COUPON_TYPE.keys()])
    percentage_off = serializers.IntegerField(min_value=1, required=False)
    amount_off = serializers.IntegerField(min_value=1, required=False)
    code = serializers.CharField(min_length=3)
    minimum_total = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    excluded_categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Categories.objects.all())
    cap = serializers.IntegerField(min_value=0)
    customer_specific = serializers.PrimaryKeyRelatedField(many=True, queryset=Customers.objects.all())
    item_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Items.objects.all())
    expiry_date = serializers.DateField()
    brand_id = serializers.IntegerField()


class CouponPutSerializer(serializers.ModelSerializer):
    excluded_categories = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), many=True)
    customer_specific = serializers.PrimaryKeyRelatedField(queryset=Customers.objects.all(), many=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Items.objects.all(), many=True)

    class Meta:
        model = CouponCodes
        fields = ['id', 'name', 'description', 'coupon_type', 'percentage_off', 'amount_off', 'code',
                  'minimum_total', 'excluded_categories', 'cap', 'customer_specific', 'item_id', 'expiry_date', 'brand_id']

class CouponDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class CouponGetSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    code = serializers.CharField(min_length=3, required=False)
    brand_id = serializers.IntegerField(required=False)
    order = serializers.ChoiceField(choices=[('asc', 'asc'), ('desc', 'desc'), ('', 'empty')], required=False)
    count = serializers.IntegerField(required=False)
    offset = serializers.IntegerField(required=False)

class CustomerCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCuponUsage
        fields = ['id', 'coupon_id', 'customer_phone', 'used_amount', 'used_count']

class InfluencerCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerCouponCodes
        fields = ['id', 'coupon_id', 'cut', 'tax', 'name', 'phone', 'email']


class CouponOutletLinkValidatior(Model):
    id = IntegerField(primary_key=True)
    coupon_id = IntegerField()
    outlet_id = IntegerField()
    visible = BooleanField()

    class Meta:
        db_table = 'coupon_outlet_connection'
        app_label = 'cart'

    @classmethod
    def get_validator(cls, body):
        from django.core.exceptions import ValidationError
        from django.forms.models import model_to_dict

        instance = cls(**model_to_dict(body))
        try:
            instance.full_clean()
        except ValidationError as e:
            return e
