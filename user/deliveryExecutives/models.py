from django.db import models

class DeliveryExecutives(models.Model):
    id = models.AutoField(primary_key=True)
    de_id = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20)
    dob = models.BigIntegerField()
    email = models.CharField(max_length=200)
    bank_details = models.JSONField()
    aadhar_no = models.IntegerField()
    aadhar_photo = models.CharField(max_length=1000)
    dl_photo = models.CharField(max_length=1000)
    dl_expiry_date = models.BigIntegerField()
    emission_expiry_date = models.BigIntegerField()
    emission_photo = models.CharField(max_length=1000)
    insurance_photo = models.CharField(max_length=1000)
    insurance_expiry_date = models.BigIntegerField()
    vehicle_photo = models.CharField(max_length=1000)
    de_photo = models.CharField(max_length=1000)
    rc_photo = models.CharField(max_length=1000)
    device_type = models.CharField(max_length=255)
    esign = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_on = models.BigIntegerField()
    modified_on = models.BigIntegerField()
    approved = models.BooleanField(default=False)

    class Meta:
        app_label = 'user'

class CheckoutAmountTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    is_addition = models.BooleanField(default=True)

    class Meta:
        app_label = 'user'

class DECheckout(models.Model):
    id = models.AutoField(primary_key=True)
    de_id = models.IntegerField()
    status = models.BooleanField(default=False)
    submitted_on = models.BigIntegerField()
    created_on = models.BigIntegerField()
    modified_on = models.BigIntegerField()
    can_edit = models.BooleanField(default=False)
    submitted_total = models.DecimalField(max_digits=10, decimal_places=2)
    orders_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'user'


class DECheckoutWithAmount(models.Model):
    id = models.AutoField(primary_key=True)
    de_checkout_id = models.IntegerField()
    checkout_amount_id = models.IntegerField()
    total_count = models.IntegerField()

    class Meta:
        app_label = 'user'


class DailyOutletCheckout(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    note = models.CharField(max_length=255)
    created_on = models.BigIntegerField()

    class Meta:
        app_label = 'user'


class DeliveryTypes(models.Model):
    id = models.AutoField(primary_key=True)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)
    earning_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.BigIntegerField()
    deleted = models.BooleanField(default=False)


    class Meta:
        app_label = 'user'