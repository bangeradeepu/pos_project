from django.db import models

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    alt_phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=255)
    email = models.EmailField()
    login_status = models.BooleanField(default=False)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    deleted = models.BooleanField(default=False)

    class Meta:
        app_label = 'customers'
 

class CustomerAddresses(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    address = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    coordinates = models.JSONField()
    type = models.CharField(max_length=255)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    deleted = models.BooleanField(default=False)


    class Meta:
        app_label = 'customers'
