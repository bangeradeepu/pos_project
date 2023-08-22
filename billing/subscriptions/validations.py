from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'price', 'duration', 'features']

    name = forms.CharField(min_length=4)
    price = forms.DecimalField()
    duration = forms.DecimalField()
    features = forms.JSONField()
