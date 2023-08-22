from django import forms

class ItemValidationForm(forms.Form):
    item_id = forms.IntegerField()
    quantity = forms.IntegerField()
    variant_id = forms.IntegerField(required=False)
    addon_variants = forms.TypedMultipleChoiceField(
        choices=[(str(i), str(i)) for i in range(1, 1000)],
        coerce=int,
        required=False,
    )

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be greater than or equal to 1.")
        return quantity

    def clean_addon_variants(self):
        addon_variants = self.cleaned_data['addon_variants']
        if len(addon_variants) == 0:
            raise forms.ValidationError("At least one addon variant is required.")
        return addon_variants

class PutValidationForm(forms.Form):
    id = forms.IntegerField()
    item_id = forms.IntegerField()
    quantity = forms.IntegerField()
    addon_variants = forms.TypedMultipleChoiceField(
        choices=[(str(i), str(i)) for i in range(1, 1000)],
        coerce=int,
        required=False,
    )

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be greater than or equal to 1.")
        return quantity

    def clean_addon_variants(self):
        addon_variants = self.cleaned_data['addon_variants']
        if len(addon_variants) == 0:
            raise forms.ValidationError("At least one addon variant is required.")
        return addon_variants

class DeleteValidationForm(forms.Form):
    id = forms.IntegerField()
