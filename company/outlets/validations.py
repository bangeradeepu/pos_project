import random
import string
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pos_project.constants import OUTLET_TYPE
from django.core.validators import RegexValidator


# Custom validator for generating a random password
def generate_random_password():
    charset = string.ascii_letters + string.digits + "!@#$%^&*()"
    password_length = 16
    return ''.join(random.choice(charset) for _ in range(password_length))

# Example usage of the custom validator
def validate_password(value):
    password = generate_random_password()
    if not password:
        raise ValidationError(_("Failed to generate a random password."))
    return password

from django import forms
from datetime import datetime

class GetValidatorForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    company_id = forms.IntegerField(required=False)
    order = forms.ChoiceField(choices=[('asc', 'asc'), ('desc', 'desc'), ('', '')], required=False)
    count = forms.IntegerField(required=False)
    offset = forms.IntegerField(required=False)

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date:
            if start_date < datetime.today().date():
                raise forms.ValidationError("Start date must be today or a future date.")
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if end_date:
            # Add any additional custom validation for end_date if needed
            if end_date < datetime.today().date():
                raise forms.ValidationError("End date must be today or a future date.")
        return end_date

class PostValidatorForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, required=True)
    owner_name = forms.CharField(min_length=3, max_length=100, required=True)
    company_id = forms.IntegerField(required=True)
    address = forms.CharField(min_length=10, required=True)
    phone_no = forms.CharField(min_length=10, validators=[RegexValidator(r'^[0-9]+$')], required=True)
    email = forms.EmailField(required=True)
    outlet_type = forms.ChoiceField(choices=[(key, key) for key in OUTLET_TYPE.keys()], required=True)
    logo = forms.CharField(min_length=3, required=True)
    gst = forms.CharField(min_length=8, required=True)
    fssai = forms.CharField(min_length=8, required=True)
    trade_license = forms.CharField(min_length=8, required=True)
    acc_name = forms.CharField(required=True)
    acc_no = forms.CharField(min_length=10, validators=[RegexValidator(r'^[0-9]+$')], required=True)
    ifsc = forms.CharField(required=True)
    bank_name = forms.CharField(required=True)
    branch = forms.CharField(required=True)

class PutValidatorForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, required=False)
    id = forms.IntegerField(required=True)
    address = forms.CharField(min_length=10, required=False)
    phone_no = forms.CharField(min_length=10, validators=[RegexValidator(r'^[0-9]+$')], required=False)
    email = forms.EmailField(required=False)
    outlet_type = forms.CharField(required=False)
    logo = forms.CharField(min_length=3, required=False)
    gst = forms.CharField(min_length=8, required=False)
    fssai = forms.CharField(min_length=8, required=False)
    trade_license = forms.CharField(min_length=8, required=False)
    acc_name = forms.CharField(required=True)
    acc_no = forms.CharField(min_length=10, validators=[RegexValidator(r'^[0-9]+$')], required=True)
    ifsc = forms.CharField(required=True)
    bank_name = forms.CharField(required=True)
    branch = forms.CharField(required=True)
