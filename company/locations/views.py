from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Location, Layer, Distance, Charges, ServiceableLocation
from .validations import LocationForm, LayerForm, DistanceForm, ChargesForm, ServiceableLocationForm,  ChargesDeleteForm

def location_json_validation(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            detection_type = form.cleaned_data['detection_type']
            lat = form.cleaned_data['lat']
            lng = form.cleaned_data['lng']

            # Save data to Location model
            location = Location.objects.create(
                detection_type=detection_type,
                lat=lat,
                lng=lng
            )

            return JsonResponse({'message': 'Location data saved successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def layers_validation(request):
    if request.method == 'POST':
        form = LayerForm(request.POST)
        if form.is_valid():
            charge_id = form.cleaned_data['charge_id']
            name = form.cleaned_data['name']
            lat = form.cleaned_data['lat']
            lng = form.cleaned_data['lng']

            # Save data to Layer model
            layer = Layer.objects.create(
                charge_id=charge_id,
                name=name,
                lat=lat,
                lng=lng
            )

            return JsonResponse({'message': 'Layer data saved successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def distances_validation(request):
    if request.method == 'POST':
        form = DistanceForm(request.POST)
        if form.is_valid():
            charge_id = form.cleaned_data['charge_id']
            name = form.cleaned_data['name']
            distance = form.cleaned_data['distance']

            # Save data to Distance model
            distance_obj = Distance.objects.create(
                charge_id=charge_id,
                name=name,
                distance=distance
            )

            return JsonResponse({'message': 'Distance data saved successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

# Define similar views for Charges and ServiceableLocation validations

def is_serviceable_validation(request):
    if request.method == 'POST':
        form = ServiceableLocationForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['lat']
            lng = form.cleaned_data['lng']

            # Check if the location is serviceable
            serviceable = ServiceableLocation.objects.filter(lat=lat, lng=lng).exists()

            return JsonResponse({'is_serviceable': serviceable})
        else:
            return JsonResponse({'errors': form.errors}, status=400)


def charges_validation(request):
    if request.method == 'POST':
        form = ChargesForm(request.POST)
        if form.is_valid():
            delivery_charge = form.cleaned_data['delivery_charge']
            earning_price = form.cleaned_data['earning_price']

            # Save data to Charges model
            charges = Charges.objects.create(
                delivery_charge=delivery_charge,
                earning_price=earning_price
            )

            return JsonResponse({'message': 'Charges data saved successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def charges_delete_validation(request):
    if request.method == 'POST':
        form = ChargesDeleteForm(request.POST)
        if form.is_valid():
            charge_id = form.cleaned_data['id']

            # Delete the specified Charges record
            try:
                charge = Charges.objects.get(id=charge_id)
                charge.delete()
                return JsonResponse({'message': 'Charges data deleted successfully'})
            except Charges.DoesNotExist:
                return JsonResponse({'error': 'Charges not found'}, status=404)
        else:
            return JsonResponse({'errors': form.errors}, status=400)