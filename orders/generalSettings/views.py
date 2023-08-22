from rest_framework import generics
from django.http import JsonResponse
from .models import Timing, Status, GeneralSettings, AdditionalCharge
from .validations import (
    TimingValidator, 
    StatusValidator,
    AdditionalChargesForm, 
    AdditionalChargesUpdateForm, 
    SettingsGetForm, 
    UpdateOutletsForm
)
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from company.outlets.models import Outlets


def timings_post_view(request):
    if request.method == 'POST':
        data = request.POST  # Replace with your data source
        try:
            TimingValidator()(data)  # Validate using the TimingValidator
            # Create Timing model instance using data
            timing = Timing(brand_id=data['brand_id'], from_time=data['from'], to_time=data['to'])
            timing.save()
            return JsonResponse({'message': 'Timing created successfully'})
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

def status_post_view(request):
    if request.method == 'POST':
        data = request.POST  # Replace with your data source
        try:
            StatusValidator()(data)  # Validate using the StatusValidator
            # Create Status model instance using data
            status = Status(brand_id=data['brand_id'], web_active=data['web']['active'], web_message=data['web']['message'], app_active=data['app']['active'], app_message=data['app']['message'])
            status.save()
            return JsonResponse({'message': 'Status created successfully'})
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)



def create_additional_charge(request):
    if request.method == 'POST':
        form = AdditionalChargesForm(request.POST)
        if form.is_valid():
            # Process form data and create AdditionalCharge instance
            additional_charge = AdditionalCharge(
                brand_id=form.cleaned_data['brand_id'],
                name=form.cleaned_data['value'][0]['name'],
                value_type=form.cleaned_data['value'][0]['value_type'],
                value=form.cleaned_data['value'][0]['value'],
                type=form.cleaned_data['value'][0]['type'],
                target=form.cleaned_data['value'][0]['target']
            )
            additional_charge.save()
            return JsonResponse({'message': 'Additional charge created successfully.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def update_additional_charge(request, charge_id):
    additional_charge = get_object_or_404(AdditionalCharge, pk=charge_id)
    if request.method == 'PUT':
        form = AdditionalChargesUpdateForm(request.PUT)
        if form.is_valid():
            # Process form data and update AdditionalCharge instance
            additional_charge.name = form.cleaned_data['value'][0]['name']
            additional_charge.value_type = form.cleaned_data['value'][0]['value_type']
            additional_charge.value = form.cleaned_data['value'][0]['value']
            additional_charge.type = form.cleaned_data['value'][0]['type']
            additional_charge.target = form.cleaned_data['value'][0]['target']
            additional_charge.save()
            return JsonResponse({'message': 'Additional charge updated successfully.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def get_general_settings(request):
    if request.method == 'GET':
        form = SettingsGetForm(request.GET)
        if form.is_valid():
            settings_type = form.cleaned_data['type']
            brand_id = form.cleaned_data.get('brand_id', None)
            if settings_type != 'DELIVERY_DETECTION':
                # Query and return general settings
                settings = GeneralSettings.objects.filter(brand_id=brand_id, setting_type=settings_type)
                serialized_settings = [{'attribute': setting.attribute, 'value': setting.value} for setting in settings]
                return JsonResponse({'settings': serialized_settings})
            else:
                return JsonResponse({'message': 'Invalid settings type.'}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def update_outlets(request):
    if request.method == 'POST':
        form = UpdateOutletsForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            for item in items:
                outlet_id = item['outlet_id'][0]  # Assuming only one outlet ID is provided
                settings = item['settings']
                outlet = Outlets.objects.get(pk=outlet_id)
                for setting_name, setting_value in settings.items():
                    outlet.bank_details[setting_name] = setting_value
                outlet.save()
            return JsonResponse({'message': 'Outlets updated successfully.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

