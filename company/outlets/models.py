from django.db import models

class Outlets(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.IntegerField()
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    outlet_type = models.IntegerField()
    schema_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)
    email = models.CharField(max_length=200)
    fssai = models.CharField(max_length=1000)
    gst = models.CharField(max_length=1000)
    trade_license = models.CharField(max_length=1000)
    primary = models.BooleanField()
    bank_details = models.JSONField()
    created_on = models.CharField(max_length=100)
    modified_on = models.CharField(max_length=100)

    class Meta:
        app_label = 'company'



class CompanyOutlets(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    outlet_name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=100)
    created_on = models.BigIntegerField()
    modified_on = models.BigIntegerField()
    deleted = models.BooleanField()


    class Meta:
        app_label = 'company'