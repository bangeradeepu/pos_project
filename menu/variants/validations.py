from django import forms

class ValidatorForms:
    @staticmethod
    def get_validator(body):
        class GetValidatorForm(forms.Form):
            order = forms.ChoiceField(choices=(('asc', 'Ascending'), ('desc', 'Descending'), ('', 'No Order')))
            count = forms.IntegerField()
            offset = forms.IntegerField()
            brand_id = forms.IntegerField()

        form = GetValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def variant_get_validator(body):
        class VariantGetValidatorForm(forms.Form):
            order = forms.ChoiceField(choices=(('asc', 'Ascending'), ('desc', 'Descending'), ('', 'No Order')))
            count = forms.IntegerField()
            offset = forms.IntegerField()
            variant_categories_id = forms.IntegerField(min_value=1)

        form = VariantGetValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def category_post_validator(body):
        class CategoryPostValidatorForm(forms.Form):
            brand_id = forms.IntegerField()
            name = forms.CharField(min_length=3)
            image = forms.CharField(min_length=3)

        form = CategoryPostValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def category_put_validator(body):
        class CategoryPutValidatorForm(forms.Form):
            id = forms.IntegerField()
            name = forms.CharField(min_length=3, max_length=100, required=False)
            visible = forms.BooleanField(required=False)
            image = forms.CharField(min_length=3, required=False)

        form = CategoryPutValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def delete_validator(body):
        class DeleteValidatorForm(forms.Form):
            id = forms.IntegerField(min_value=1)

        form = DeleteValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def update_outlet_validator(body):
        class UpdateOutletValidatorForm(forms.Form):
            data = forms.DictField()
            outlets = forms.ListField()

        form = UpdateOutletValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def variant_post_validator(body):
        class VariantPostValidatorForm(forms.Form):
            name = forms.CharField(min_length=3)
            variant_categories_id = forms.IntegerField(min_value=1)
            image = forms.CharField(min_length=3)

        form = VariantPostValidatorForm(body)
        return form.is_valid(), form.errors

    @staticmethod
    def variant_put_validator(body):
        class VariantPutValidatorForm(forms.Form):
            name = forms.CharField(min_length=3, required=False)
            variant_id = forms.IntegerField(min_value=1)
            visible = forms.BooleanField(required=False)
            image = forms.CharField(min_length=3, required=False)

        form = VariantPutValidatorForm(body)
        return form.is_valid(), form.errors
