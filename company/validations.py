from django import forms

def password_generator():
    import random
    charset = 'abcdef!@#$%^&ghijklmnopqrstuvwxy!@#$%^&*()zABCDEFGHIJKLMNOPQRS!@#$%^&*(TUVWXYZ0123456789!@#$%^&**()_+!@#$%^&*()'
    return ''.join(random.choice(charset) for _ in range(16))

class CompanyForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    user_id = forms.IntegerField(required=False)
    order = forms.ChoiceField(choices=[('asc', 'asc'), ('desc', 'desc'), ('', '')], required=False)
    count = forms.IntegerField(required=False)
    offset = forms.IntegerField(required=False)

class AddCompanyForm(forms.Form):
    user_id = forms.IntegerField(error_messages={
        'invalid': 'User ID must be a number',
        'required': 'User ID is required',
    })
    name = forms.CharField()
    phone_no = forms.CharField()
    address = forms.CharField()
    logo = forms.CharField()
    email_id = forms.EmailField()
    owner_name = forms.CharField()
    owner_phone = forms.CharField()
    db_id = forms.IntegerField(required=False)

class UpdateCompanyForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(required=False)
    phone_no = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email_id = forms.EmailField(required=False)
    owner_name = forms.CharField(required=False)
    owner_phone = forms.CharField(required=False)
    db_id = forms.IntegerField(required=False)

validations = {
    'getCompanyValidation': CompanyForm,
    'addCompanyValidation': AddCompanyForm,
    'updateCompanyValidation': UpdateCompanyForm,
    'passwordGenerator': password_generator,
}
