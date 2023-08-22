from django.db import models

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    display_in = models.CharField(max_length=255)  # PLATFORM FOR THIS TO BE AVAILABLE ON (APP/WEB/INTERNAL)
    image = models.CharField(max_length=255)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=False)
    brand_id = models.IntegerField()
    mrp_items = models.BooleanField(default=False)
    single_unavailable = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        app_label = 'menu'


class CategoryOutletLink(models.Model):
    id = models.AutoField(primary_key=True)
    outlet_id = models.IntegerField()
    category_id = models.IntegerField()
    rank = models.IntegerField()
    visible = models.BooleanField(default=False)


    class Meta:
        app_label = 'menu'