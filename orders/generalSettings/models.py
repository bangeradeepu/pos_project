from django.db import models
from pos_project import constants 

class GeneralSettings(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.CharField(max_length=100)
    value = models.JSONField()
    brand_id = models.IntegerField()


    class Meta:
        app_label = 'orders'


class Timing(models.Model):
    brand_id = models.IntegerField()
    from_time = models.TimeField()
    to_time = models.TimeField()

    class Meta:
        app_label = 'orders'


class Status(models.Model):
    brand_id = models.IntegerField()
    web_active = models.BooleanField()
    web_message = models.CharField(max_length=255)
    app_active = models.BooleanField()
    app_message = models.CharField(max_length=255)

    class Meta:
        app_label = 'orders'


class Outlet(models.Model):
    outlet_id = models.IntegerField()

    class Meta:
        app_label = 'orders'

class OutletSettings(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    setting_name = models.CharField(max_length=50)  # Adjust max_length as needed
    setting_value = models.DecimalField(max_digits=10, decimal_places=2) 

    class Meta:
        app_label = 'orders'

class AdditionalCharge(models.Model):
    brand_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value_type = models.CharField(max_length=50, choices=constants.ADDITIONAL_CHARGES_KEYS['VALUE_TYPE'].items())
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50, choices=constants.ADDITIONAL_CHARGES_KEYS['TYPE'].items())
    target = models.CharField(max_length=50, choices=constants.ADDITIONAL_CHARGES_KEYS['TARGET'].items())

    class Meta:
        app_label = 'orders'
