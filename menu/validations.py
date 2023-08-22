from django import forms
from django.core.exceptions import ValidationError
from pos_project import constants 
import json


class ComboValidatorForm(forms.Form):
    id = forms.IntegerField()
    combos = forms.CharField(widget=forms.Textarea)

    def clean_combos(self):
        combos_data = self.cleaned_data.get('combos', '')

        # Convert the JSON string into a list of dictionaries
        try:
            combos = json.loads(combos_data)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data for combos')

        for combo in combos:
            if not combo.get('item_id'):
                raise ValidationError('item_id is required for each combo')
        
        return combos

class ComboDeleteValidatorForm(forms.Form):
    id = forms.IntegerField()
    combos = forms.CharField(widget=forms.Textarea)

    def clean_combos(self):
        combos_data = self.cleaned_data.get('combos', '')

        # Convert the JSON string into a list of dictionaries
        try:
            combos = json.loads(combos_data)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data for combos')

        for combo in combos:
            if not combo.get('item_id'):
                raise ValidationError('item_id is required for each combo')
        
        return combos

class GetValidatorForm(forms.Form):
    order = forms.ChoiceField(choices=(('asc', 'asc'), ('desc', 'desc'), ('', '')), required=False)
    count = forms.IntegerField(required=False)
    offset = forms.IntegerField(required=False)

class PostValidatorForm(forms.Form):
    name = forms.CharField(min_length=3)
    description = forms.CharField(min_length=6)
    category_id = forms.IntegerField(min_value=1)
    food_tag = forms.ChoiceField(choices=((tag, tag) for tag in constants.FOOD_TAG.keys()))
    price = forms.DecimalField(min_value=0)
    media_url = forms.CharField(min_length=3)
    item_type = forms.ChoiceField(choices=((item_type, item_type) for item_type in constants.ITEM_TYPE.keys()))

class PutValidatorForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(min_length=3, required=False)
    description = forms.CharField(min_length=6, required=False)
    food_tag = forms.ChoiceField(choices=((tag, tag) for tag in constants.FOOD_TAG.keys()), required=False)
    price = forms.DecimalField(min_value=0, required=False)
    media_url = forms.CharField(min_length=3, required=False)

class DeleteValidatorForm(forms.Form):
    id = forms.IntegerField()


class VariantPostValidatorForm(forms.Form):
    id = forms.IntegerField()
    variants = forms.CharField(widget=forms.Textarea)

    def clean_variants(self):
        variants_data = self.cleaned_data.get('variants', '')

        # Convert the JSON string into a list of dictionaries
        try:
            variants = json.loads(variants_data)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data for variants')

        for variant in variants:
            if not variant.get('variant_id'):
                raise ValidationError('variant_id is required for each variant')
            price = variant.get('price')
            if price is None or price < 0:
                raise ValidationError('Price must be greater than or equal to 0')

        return variants


class VariantPutValidatorForm(forms.Form):
    variant_data = forms.CharField(widget=forms.Textarea)

    def clean_variant_data(self):
        variant_data_str = self.cleaned_data.get('variant_data', '')

        try:
            variant_data = json.loads(variant_data_str)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data for variant_data')

        if not variant_data:
            raise ValidationError('At least one variant must be provided')

        for variant in variant_data:
            item_variant = variant.get('item_variant', {})
            if not item_variant.get('id'):
                raise ValidationError('id is required for each item_variant')
            price = item_variant.get('price')
            if price is not None and price < 0:
                raise ValidationError('Price must be greater than or equal to 0')

        return variant_data

class VariantDeleteValidatorForm(forms.Form):
    id = forms.IntegerField()
    variants = forms.CharField(widget=forms.Textarea)

    def clean_variants(self):
        variants_str = self.cleaned_data.get('variants', '')

        try:
            variants = json.loads(variants_str)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data for variants')

        if not variants:
            raise ValidationError('At least one variant must be provided')

        return variants


class UpdateOutletValidatorForm(forms.Form):
    outlet_data = forms.CharField(widget=forms.Textarea)

    def clean_outlet_data(self):
        outlet_data_str = self.cleaned_data.get('outlet_data', '')

        try:
            outlet_data = json.loads(outlet_data_str)
        except json.JSONDecodeError:
            raise forms.ValidationError('Invalid JSON data for outlet_data')

        if not outlet_data:
            raise forms.ValidationError('At least one outlet data must be provided')

        for data in outlet_data:
            item_id = data.get('item_id')
            if item_id is None:
                raise forms.ValidationError('item_id is required for each outlet data')

            price = data.get('price')
            if price is not None and price < 0:
                raise forms.ValidationError('Price must be greater than or equal to 0')

            strike_price = data.get('strike_price')
            if strike_price is not None and strike_price < 0:
                raise forms.ValidationError('Strike price must be greater than or equal to 0')

            rank = data.get('rank')
            if rank is not None and rank < 1:
                raise forms.ValidationError('Rank must be greater than or equal to 1')

        return outlet_data

class AddonsPostValidatorForm(forms.Form):
    id = forms.IntegerField()
    addons = forms.CharField(widget=forms.Textarea)

    def clean_addons(self):
        addons_str = self.cleaned_data.get('addons', '')

        try:
            addons = json.loads(addons_str)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data for addons')

        if not addons:
            raise ValidationError('At least one addon must be provided')

        return addons
