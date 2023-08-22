from django.db import models

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)
    features = models.JSONField()

    class Meta:
        app_label = 'billing'


class ActiveSubscriptions(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Cancelled', 'Cancelled'),
    )

    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    subscription_id = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    renewed_on = models.DecimalField(max_digits=10, decimal_places=2)
    cancelled_on = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_on = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=255)
    
    class Meta:
        app_label = 'billing'

class PaymentDetails(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    )

    id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    transaction_hash = models.CharField(max_length=255)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'billing'