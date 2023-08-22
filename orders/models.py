from django.db import models

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    order_status = models.CharField(max_length=100)
    epoch_time = models.BigIntegerField()
    created_on = models.BigIntegerField()
    modified_on = models.BigIntegerField()
    pre_order_time = models.BigIntegerField()
    de_id = models.IntegerField()
    location = models.JSONField()
    delivery_type_id = models.IntegerField()
    note = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20)
    address_id = models.IntegerField()
    coupon_id = models.IntegerField()
    coupon_details = models.JSONField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tip = models.IntegerField()
    additional_charges = models.JSONField()
    contactless = models.BooleanField(default=False)
    cancel_reason = models.CharField(max_length=255)
    platform_details = models.JSONField()
    visible = models.BooleanField(default=True)
    payment_mode = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    invoice_id = models.IntegerField()
    third_party_service_id = models.IntegerField(
        help_text='This is used for storing third party service id'
    )
    third_party_service_type = models.BooleanField(
        default=False,
        help_text='This is used for toggling external delivery executives for the order'
    )
    order_type = models.CharField(max_length=100)

    class Meta:
        app_label = 'orders'

class OrdersEdited(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    orders = models.JSONField()
    items = models.JSONField()
    created_on = models.BigIntegerField()
    user_id = models.IntegerField()
    type = models.CharField(max_length=100)


    class Meta:
        app_label = 'orders'

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    item_variant_name = models.CharField(max_length=255)
    addon_variants = models.JSONField()
    addons_total = models.IntegerField()
    total = models.IntegerField()
    brand_id = models.IntegerField()


    class Meta:
        app_label = 'orders'

class OrderTimeline(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order = models.JSONField()
    status = models.IntegerField()
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField()


    class Meta:
        app_label = 'orders'

class OrderOnlinePayment(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    payment_data = models.JSONField()
    status = models.CharField(max_length=100)
    timeframe = models.CharField(max_length=100)
    payment_service = models.CharField(max_length=100)

    class Meta:
        app_label = 'orders'


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    type = models.CharField(max_length=100)
    type_id = models.IntegerField()
    stars = models.IntegerField()
    review = models.TextField()
    photos = models.JSONField()
    created_on = models.BigIntegerField()


    class Meta:
        app_label = 'orders'