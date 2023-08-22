from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    variant_id = models.IntegerField()
    addon_variants = models.JSONField()
    created_on = models.BigIntegerField()
    modified_on = models.BigIntegerField()


    class Meta:
        app_label = 'cart'

