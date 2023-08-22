from django.db import models


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category_id = models.IntegerField()
    food_tag = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    media_url = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        app_label = 'menu'


class ItemAddonLink(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    addon_variant_id = models.IntegerField()


    class Meta:
        app_label = 'menu'



class ItemVariantLink(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    variant_id = models.IntegerField()


    class Meta:
        app_label = 'menu'


class ItemOutletLink(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    outlet_id = models.IntegerField()
    item_id = models.IntegerField()
    rank = models.IntegerField()
    visible = models.BooleanField(default=True)
    sold_out = models.BooleanField(default=False)
    unit = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    strike_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'menu'


class ComboItemsLink(models.Model):
    id = models.AutoField(primary_key=True)
    combo_id = models.IntegerField()
    item_id = models.IntegerField()
    qty = models.IntegerField()


    class Meta:
        app_label = 'menu'







