from rest_framework import generics
from .models import Brand, UserCompanyConnection

from .validations import validations
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View



class BrandCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        company_form = validations['addCompanyValidation'](data)
        if company_form.is_valid():
            data = company_form.cleaned_data
            brand = Brand(
                user_id=data['user_id'],
                name=data['name'],
                phone_no=data['phone_no'],
                address=data['address'],
                logo=data['logo'],
                email_id=data['email_id'],
                owner_name=data['owner_name'],
                owner_phone=data['owner_phone'],
                db_id=data['db_id'],
                created_on=data['created_on']
            )
            brand.save()
            return JsonResponse({'message': 'Brand created successfully!'})
        else:
            return JsonResponse({'errors': company_form.errors}, status=400)

class BrandUpdateView(View):
    def put(self, request, *args, **kwargs):
        brand_id = kwargs.get('brand_id')
        try:
            brand = Brand.objects.get(id=brand_id)
            data = request.POST.dict()
            company_form = validations['updateCompanyValidation'](data)
            if company_form.is_valid():
                data = company_form.cleaned_data
                brand.user_id = data['user_id']
                brand.name = data['name']
                brand.phone_no = data['phone_no']
                brand.address = data['address']
                brand.logo = data['logo']
                brand.email_id = data['email_id']
                brand.owner_name = data['owner_name']
                brand.owner_phone = data['owner_phone']
                brand.db_id = data['db_id']
                brand.created_on = data['created_on']
                brand.save()
                return JsonResponse({'message': 'Brand updated successfully!'})
            else:
                return JsonResponse({'errors': company_form.errors}, status=400)
        except Brand.DoesNotExist:
            return JsonResponse({'error': 'Brand not found'}, status=404)

class BrandDeleteView(View):
    def delete(self, request, *args, **kwargs):
        brand_id = kwargs.get('brand_id')
        try:
            brand = Brand.objects.get(id=brand_id)
            brand.delete()
            return JsonResponse({'message': 'Brand deleted successfully!'})
        except Brand.DoesNotExist:
            return JsonResponse({'error': 'Brand not found'}, status=404)

class BrandRetrieveView(View):
    def get(self, request, *args, **kwargs):
        brand_id = kwargs.get('brand_id')
        try:
            brand = Brand.objects.get(id=brand_id)
            data = {
                'id': brand.id,
                'user_id': brand.user_id,
                'name': brand.name,
                'phone_no': brand.phone_no,
                'address': brand.address,
                'logo': brand.logo,
                'email_id': brand.email_id,
                'owner_name': brand.owner_name,
                'owner_phone': brand.owner_phone,
                'db_id': brand.db_id,
                'created_on': brand.created_on,
            }
            return JsonResponse(data)
        except Brand.DoesNotExist:
            return JsonResponse({'error': 'Brand not found'}, status=404)

class UserCompanyConnectionCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        user_company_form = validations['updateCompanyValidation'](data)
        if user_company_form.is_valid():
            data = user_company_form.cleaned_data
            user_company_connection = UserCompanyConnection(
                user_id=data['user_id'],
                company_id=data['company_id']
            )
            user_company_connection.save()
            return JsonResponse({'message': 'User-Company connection created successfully!'})
        else:
            return JsonResponse({'errors': user_company_form.errors}, status=400)

class UserCompanyConnectionUpdateView(View):
    def put(self, request, *args, **kwargs):
        connection_id = kwargs.get('connection_id')
        try:
            connection = UserCompanyConnection.objects.get(id=connection_id)
            data = request.POST.dict()
            connection_form = validations['updateCompanyValidation'](data)
            if connection_form.is_valid():
                data = connection_form.cleaned_data
                connection.user_id = data['user_id']
                connection.company_id = data['company_id']
                connection.save()
                return JsonResponse({'message': 'User-Company connection updated successfully!'})
            else:
                return JsonResponse({'errors': connection_form.errors}, status=400)
        except UserCompanyConnection.DoesNotExist:
            return JsonResponse({'error': 'User-Company connection not found'}, status=404)

class UserCompanyConnectionDeleteView(View):
    def delete(self, request, *args, **kwargs):
        connection_id = kwargs.get('connection_id')
        try:
            connection = UserCompanyConnection.objects.get(id=connection_id)
            connection.delete()
            return JsonResponse({'message': 'User-Company connection deleted successfully!'})
        except UserCompanyConnection.DoesNotExist:
            return JsonResponse({'error': 'User-Company connection not found'}, status=404)

class UserCompanyConnectionRetrieveView(View):
    def get(self, request, *args, **kwargs):
        connection_id = kwargs.get('connection_id')
        try:
            connection = UserCompanyConnection.objects.get(id=connection_id)
            data = {
                'user_id': connection.user_id,
                'company_id': connection.company_id,
            }
            return JsonResponse(data)
        except UserCompanyConnection.DoesNotExist:
            return JsonResponse({'error': 'User-Company connection not found'}, status=404)

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Brand
from .outlets.models import Outlets
from .location_service import init_delivery_type, get_distance_from_outlet, get_location_details, create_nearest_outlet_promise

def get_location_details_view(request):
    try:
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        brand_id = int(request.GET.get('brand_id'))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)

    brand = get_object_or_404(Brand, id=brand_id)
    coordinates = {'lat': lat, 'lng': lng}
    details = get_location_details(coordinates, brand)

    return JsonResponse({'details': details})

def get_distance_from_outlet_view(request):
    try:
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        outlet_id = int(request.GET.get('outlet_id'))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)

    outlet = get_object_or_404(Outlets, id=outlet_id)
    coordinates = {'lat': lat, 'lng': lng}
    distance = get_distance_from_outlet(coordinates, outlet.coordinates)

    return JsonResponse({'distance': distance})

def init_delivery_type_view(request):
    try:
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        brand_id = int(request.GET.get('brand_id'))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)

    brand = get_object_or_404(Brand, id=brand_id)
    location_settings = brand.location_settings
    layers_settings = brand.layers_settings
    distances_settings = brand.distances_settings

    try:
        coordinates = {'lat': lat, 'lng': lng}
        delivery_type = init_delivery_type(location_settings, coordinates, layers_settings, distances_settings)
        return JsonResponse({'delivery_type': delivery_type})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def create_nearest_outlet_promise_view(request):
    try:
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        outlet = request.GET.get('outlet')
        outlet_origin = request.GET.get('outlet_origin')  # Adjust as needed

        coordinates = {'lat': lat, 'lng': lng}
        outlet_origin = {'lat': float(outlet_origin['lat']), 'lng': float(outlet_origin['lng'])}  # Convert to float

        result = create_nearest_outlet_promise(coordinates, outlet, outlet_origin)
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
