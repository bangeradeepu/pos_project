from rest_framework import generics
from .models import Brands, OutletBrandsLink
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .validations import (
    validate_get_request,
    validate_post_request,
    validate_put_request,
    validate_delete_request,
    validate_outlet_brand_request,
)

def get_brands(request):
    errors = validate_get_request(request)
    if errors:
        return JsonResponse({'error': errors}, status=400)

    order = request.GET.get('order', None)
    count = request.GET.get('count', None)
    offset = request.GET.get('offset', None)

    # Filtering the brands based on the order parameter
    if order in ('asc', 'desc'):
        order_sign = '' if order == 'asc' else '-'
        brands = Brands.objects.order_by(f'{order_sign}created_on')
    else:
        brands = Brands.objects.all()

    # Pagination based on count and offset parameters
    if count is not None and offset is not None:
        try:
            count = int(count)
            offset = int(offset)
            brands = brands[offset : offset + count]
        except ValueError:
            return JsonResponse({'error': 'Invalid count or offset parameters'}, status=400)

    # Generating the list of brand data to be returned in the response
    brands_data = [{'id': brand.id, 'name': brand.name} for brand in brands]

    return JsonResponse({'brands': brands_data})

def create_brand(request):
    errors = validate_post_request(request)
    if errors:
        return JsonResponse({'error': errors}, status=400)

    name = request.POST['name']

    # Check if a brand with the same name already exists
    if Brands.objects.filter(name=name).exists():
        return JsonResponse({'error': 'Brand with this name already exists'}, status=400)

    try:
        # Create a new brand instance
        brand = Brands(name=name, created_on=123456789, modified_on=123456789, deleted=False)
        brand.save()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Brand created successfully'})

def delete_brand(request):
    errors = validate_delete_request(request)
    if errors:
        return JsonResponse({'error': errors}, status=400)

    brand_id = request.POST['id']

    try:
        # Get the brand with the given brand_id
        brand = Brands.objects.get(id=brand_id)
        # Perform a logical delete by marking the 'deleted' field as True
        brand.deleted = True
        brand.save()
    except Brands.DoesNotExist:
        return JsonResponse({'error': 'Brand not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Brand deleted successfully'})

def update_brand(request):
    errors = validate_put_request(request)
    if errors:
        return JsonResponse({'error': errors}, status=400)

    brand_id = request.POST['id']
    name = request.POST['name']

    try:
        # Get the brand with the given brand_id
        brand = Brands.objects.get(id=brand_id)
        # Update the brand name
        brand.name = name
        brand.save()
    except Brands.DoesNotExist:
        return JsonResponse({'error': 'Brand not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Brand updated successfully'})

def add_brand_to_outlet(request):
    errors = validate_outlet_brand_request(request)
    if errors:
        return JsonResponse({'error': errors}, status=400)

    brand_id = request.POST['brand_id']
    outlet_id = request.POST['outlet_id']

    try:
        # Check if the brand and outlet exist before adding the link
        brand = Brands.objects.get(id=brand_id)
        # You might need to replace 'Outlet' with the actual name of your Outlet model
        outlet = OutletBrandsLink.objects.get(id=outlet_id)

        # Create a new link between the brand and outlet
        link = OutletBrandsLink(brand_id=brand_id, outlet_id=outlet_id)
        link.save()
    except Brands.DoesNotExist:
        return JsonResponse({'error': 'Brand not found'}, status=404)
    except OutletBrandsLink.DoesNotExist:
        return JsonResponse({'error': 'Outlet not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Brand added to the outlet'})

def remove_brand_from_outlet(request):
    errors = validate_outlet_brand_request(request)
    if errors:
        return JsonResponse({'error': errors}, status=400)

    brand_id = request.PUT['brand_id']
    outlet_id = request.PUT['outlet_id']

    try:
        # Check if the brand and outlet exist before removing the link
        brand = Brands.objects.get(id=brand_id)
        # You might need to replace 'Outlet' with the actual name of your Outlet model
        outlet = OutletBrandsLink.objects.get(id=outlet_id)

        # Remove the link between the brand and outlet
        OutletBrandsLink.objects.filter(brand_id=brand_id, outlet_id=outlet_id).delete()
    except Brands.DoesNotExist:
        return JsonResponse({'error': 'Brand not found'}, status=404)
    except OutletBrandsLink.DoesNotExist:
        return JsonResponse({'error': 'Outlet not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Brand removed from the outlet'})