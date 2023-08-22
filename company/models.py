from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)
    email_id = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=255)
    db_id = models.IntegerField()
    created_on = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'company'

class UserCompanyConnection(models.Model):
    user_id = models.DecimalField(max_digits=10, decimal_places=2)
    company_id = models.CharField(max_length=255)


    class Meta:
        app_label = 'company'

