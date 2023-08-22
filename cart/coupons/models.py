from django.db import models

class CouponCodes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    coupon_type = models.CharField(max_length=255)
    percentage_off = models.IntegerField()
    amount_off = models.IntegerField()
    code = models.CharField(max_length=255)
    minimum_total = models.IntegerField()
    excluded_categories = models.JSONField()
    cap = models.IntegerField()
    customer_specific = models.JSONField()
    item_id = models.JSONField()
    created_on = models.BigIntegerField()
    expiry_on = models.BigIntegerField()
    brand_id = models.IntegerField()

    class Meta:
        app_label = 'cart'


class CustomerCuponUsage(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    customer_phone = models.CharField(max_length=255)
    used_amount = models.IntegerField()
    used_count = models.IntegerField()

    class Meta:
        app_label = 'cart'



class InfluencerCouponCodes(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    cut = models.IntegerField()
    tax = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        app_label = 'cart'



class CouponOutletLink(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    outlet_id = models.IntegerField()
    visible = models.BooleanField()


    class Meta:
        app_label = 'cart'

