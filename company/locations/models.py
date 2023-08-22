from django.db import models

class Location(models.Model):
    detection_type = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        app_label = 'company'


class Layer(models.Model):
    charge_id = models.IntegerField()
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        app_label = 'company'


class Distance(models.Model):
    charge_id = models.IntegerField()
    name = models.CharField(max_length=100)
    distance = models.FloatField()

    class Meta:
        app_label = 'company'
 
    

class Charges(models.Model):
    delivery_charge = models.FloatField()
    earning_price = models.FloatField()

    class Meta:
        app_label = 'company'



class ServiceableLocation(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        app_label = 'company'
