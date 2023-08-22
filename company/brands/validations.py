from django import forms

class GetValidationForm(forms.Form):
    order = forms.ChoiceField(choices=[('asc', 'Ascending'), ('desc', 'Descending'), ('', 'None')], required=False)
    count = forms.IntegerField(required=False)
    offset = forms.IntegerField(required=False)

class PostValidationForm(forms.Form):
    name = forms.CharField()

class PutValidationForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()

class DeleteValidationForm(forms.Form):
    id = forms.IntegerField()

class OutletBrandValidationForm(forms.Form):
    brand_id = forms.IntegerField()
    outlet_id = forms.IntegerField()

def validate_get_request(request):
    form = GetValidationForm(request.GET)
    if not form.is_valid():
        return form.errors
    return None

def validate_post_request(request):
    form = PostValidationForm(request.POST)
    if not form.is_valid():
        return form.errors
    return None

def validate_put_request(request):
    form = PutValidationForm(request.POST)
    if not form.is_valid():
        return form.errors
    return None

def validate_delete_request(request):
    form = DeleteValidationForm(request.POST)
    if not form.is_valid():
        return form.errors
    return None

def validate_outlet_brand_request(request):
    if request.method == 'POST':
        form = OutletBrandValidationForm(request.POST)
    elif request.method == 'PUT':
        form = OutletBrandValidationForm(request.PUT)

    if not form.is_valid():
        return form.errors
    return None
