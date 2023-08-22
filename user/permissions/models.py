from django.db import models

class Permissions(models.Model):
    role_id = models.IntegerField(primary_key=True)
    module_id = models.IntegerField()
    create = models.BooleanField()
    read = models.BooleanField()
    update = models.BooleanField()
    delete = models.BooleanField()

    class Meta:
        app_label = 'user'

class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'user'

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_on = models.BigIntegerField()

    class Meta:
        app_label = 'user'

class UserRoles(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()
    company_id = models.IntegerField()
    outlet_id = models.IntegerField()

    class Meta:
        app_label = 'user'

