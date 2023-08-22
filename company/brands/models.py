from django.db import models

class Brands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_on = models.BigIntegerField()
    modified_on = models.BigIntegerField()
    deleted = models.BooleanField()

    class Meta:
        app_label = 'company'
 


class OutletBrandsLink(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    brand_id = models.IntegerField()

    class Meta:
        app_label = 'company'


