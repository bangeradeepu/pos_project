from django import forms

class AddPermissionsForm(forms.Form):
    role_id = forms.IntegerField()
    module_id = forms.IntegerField()
    create = forms.BooleanField()
    read = forms.BooleanField()
    update = forms.BooleanField()
    delete = forms.BooleanField()

class DeletePermissionsForm(forms.Form):
    role_id = forms.IntegerField()
    module_id = forms.IntegerField(required=False)

class AddRoleForm(forms.Form):
    name = forms.CharField(min_length=3)

class AddRoleToUserForm(forms.Form):
    role_id = forms.IntegerField()
    user_id = forms.IntegerField()
    outlet_id = forms.IntegerField()
