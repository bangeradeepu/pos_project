from django import forms
from django.core.exceptions import ValidationError

class LocationForm(forms.Form):
    detection_type = forms.CharField(max_length=50)
    lat = forms.FloatField()
    lng = forms.FloatField()

class LayerForm(forms.Form):
    charge_id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    lat = forms.FloatField()
    lng = forms.FloatField()

    def clean(self):
        cleaned_data = super().clean()
        lat = cleaned_data.get('lat')
        lng = cleaned_data.get('lng')
        if lat is None or lng is None:
            raise ValidationError("Both lat and lng are required.")

class DistanceForm(forms.Form):
    charge_id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    distance = forms.FloatField()

class ServiceableLocationForm(forms.Form):
    lat = forms.FloatField()
    lng = forms.FloatField()

class ChargesForm(forms.Form):
    delivery_charge = forms.FloatField(min_value=0)
    earning_price = forms.FloatField(min_value=0)

class ChargesDeleteForm(forms.Form):
    id = forms.IntegerField()