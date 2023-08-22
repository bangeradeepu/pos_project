from django.db import models

class AddonCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=True)
    brand_id = models.IntegerField()
    deleted = models.BooleanField(default=False)


    class Meta:
        app_label = 'menu'


class AddonVariants(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    addon_categories_id = models.IntegerField()
    food_tag = models.CharField(max_length=10)
    image = models.CharField(max_length=1000)
    created_on = models.CharField(max_length=50)
    modified_on = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)


    class Meta:
        app_label = 'menu'

class AddonCategoryOutletLink(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    addon_categories_id = models.IntegerField()
    visible = models.BooleanField(default=True)

    class Meta:
        app_label = 'menu'


class AddonVariantOutletLink(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    addon_variant_id = models.IntegerField()
    visible = models.BooleanField(default=True)
    sold_out = models.BooleanField(default=False)



    class Meta:
        app_label = 'menu'