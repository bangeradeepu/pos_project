from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from .models import CheckoutAmountTypes, DECheckout

class CheckoutAmountTypesForm(forms.ModelForm):
    class Meta:
        model = CheckoutAmountTypes
        fields = ['name', 'value']

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 0:
            raise ValidationError("Value must be greater than or equal to 0.")
        return value

class DECheckoutForm(forms.ModelForm):
    class Meta:
        model = DECheckout
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        submitted_total = cleaned_data.get('submitted_total', 0)
        orders_total = cleaned_data.get('orders_total', 0)

        if submitted_total < orders_total:
            raise ValidationError("Submitted total must be greater than or equal to orders total.")
        return cleaned_data
        
class CheckoutPostForm(forms.Form):
    user_id = forms.IntegerField()
    amounts = forms.ModelMultipleChoiceField(
        queryset=CheckoutAmountTypes.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        error_messages={'required': 'You must select at least one amount.'}
    )

    def clean_amounts(self):
        amounts = self.cleaned_data['amounts']
        if len(amounts) != len(set(amounts)):
            raise ValidationError('Checkout amounts must be unique.')
        return amounts

class CheckoutPutForm(forms.Form):
    de_checkout_id = forms.IntegerField()
    user_id = forms.IntegerField()
    amounts = forms.ModelMultipleChoiceField(
        queryset=CheckoutAmountTypes.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        error_messages={'required': 'You must select at least one amount.'}
    )

    def clean_amounts(self):
        amounts = self.cleaned_data['amounts']
        if len(amounts) != len(set(amounts)):
            raise ValidationError('Checkout amounts must be unique.')
        return amounts

class CheckoutStatusForm(forms.Form):
    de_checkout_id = forms.IntegerField()
    status = forms.BooleanField()

class CheckoutSubmitForm(forms.Form):
    note = forms.CharField(required=False, widget=forms.Textarea)

from django import forms
from django.core.validators import MinLengthValidator

class CustomForm(forms.Form):
    logged_in = forms.BooleanField(required=False)
    approved_only = forms.BooleanField(required=False)
    all = forms.BooleanField(required=False)
    order = forms.ChoiceField(choices=[('', ''), ('asc', 'asc'), ('desc', 'desc')], required=False)
    count = forms.IntegerField(required=False)
    offset = forms.IntegerField(required=False)

    user_id = forms.IntegerField()
    name = forms.CharField(min_length=3, required=False)
    address = forms.CharField(min_length=10, required=False)
    phone = forms.CharField(min_length=10, required=False)
    alternate_phone = forms.CharField(min_length=10, required=False)
    dob = forms.IntegerField(required=False)
    email = forms.EmailField(min_length=3, required=False)
    bank_details = forms.JSONField(required=False)
    aadhar_no = forms.IntegerField(validators=[MinLengthValidator(12)], required=False)
    aadhar_photo = forms.CharField(min_length=3, required=False)
    dl_photo = forms.CharField(min_length=3, required=False)
    dl_expiry_date = forms.IntegerField(required=False)
    emission_expiry_date = forms.IntegerField(required=False)
    emission_photo = forms.CharField(min_length=3, required=False)
    insurance_photo = forms.CharField(min_length=3, required=False)
    insurance_expiry_date = forms.IntegerField(required=False)
    vehicle_photo = forms.CharField(min_length=3, required=False)
    de_photo = forms.CharField(min_length=3, required=False)
    rc_photo = forms.CharField(min_length=3, required=False)
    device_type = forms.CharField(min_length=3, required=False)
    esign = forms.CharField(min_length=3, required=False)
    approved = forms.BooleanField(required=False)
    status = forms.BooleanField(required=False)

class PutValidationForm(forms.Form):
    user_id = forms.IntegerField()
    name = forms.CharField(min_length=3, required=False)
    address = forms.CharField(min_length=10, required=False)
    phone = forms.CharField(min_length=10, required=False)
    alternate_phone = forms.CharField(min_length=10, required=False)
    dob = forms.IntegerField(required=False)
    email = forms.EmailField(min_length=3, required=False)
    bank_details = forms.JSONField(required=False)
    aadhar_no = forms.IntegerField(validators=[MinLengthValidator(12)], required=False)
    aadhar_photo = forms.CharField(min_length=3, required=False)
    dl_photo = forms.CharField(min_length=3, required=False)
    dl_expiry_date = forms.IntegerField(required=False)
    emission_expiry_date = forms.IntegerField(required=False)
    emission_photo = forms.CharField(min_length=3, required=False)
    insurance_photo = forms.CharField(min_length=3, required=False)
    insurance_expiry_date = forms.IntegerField(required=False)
    vehicle_photo = forms.CharField(min_length=3, required=False)
    de_photo = forms.CharField(min_length=3, required=False)
    rc_photo = forms.CharField(min_length=3, required=False)
    device_type = forms.CharField(min_length=3, required=False)
    esign = forms.CharField(min_length=3, required=False)
    approved = forms.BooleanField(required=False)
    status = forms.BooleanField(required=False)

class DeleteValidationForm(forms.Form):
    user_id = forms.IntegerField()

class OutletBrandValidationForm(forms.Form):
    brand_id = forms.IntegerField()
    outlet_id = forms.IntegerField()
