from django.db import models

class VariantCategories(models.Model):
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

class Variants(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    variant_categories_id = models.IntegerField()
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)


    class Meta:
        app_label = 'menu'

class VariantCategoryOutletLink(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    variant_categories_id = models.IntegerField()
    visible = models.BooleanField(default=True)

 
    class Meta:
        app_label = 'menu'


class VariantOuletLink(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    variant_id = models.IntegerField()
    visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_out = models.BooleanField(default=False)



    class Meta:
        app_label = 'menu'