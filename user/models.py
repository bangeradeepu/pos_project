from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_on = models.DecimalField(max_digits=10, decimal_places=2)
    modified_on = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    level = models.IntegerField()
    loggedin_details = models.JSONField()

    class Meta:
        app_label = 'user'

class UserCompanyLink(models.Model):
    user_id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    outlet_id = models.IntegerField()


    class Meta:
        app_label = 'user'
