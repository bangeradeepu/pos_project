from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import VariantCategories, Variants, VariantCategoryOutletLink, VariantOuletLink
from .validations import ValidatorForms

@csrf_exempt
def update_outlet(request):
    if request.method == 'POST':
        is_valid, errors = ValidatorForms.update_outlet_validator(request.POST)
        if is_valid:
            data = request.POST.get('data')
            for item in data:
                outlet_id = item['id']
                visible = item['visible']
                outlet_category = get_object_or_404(VariantCategoryOutletLink, outlet_id=outlet_id)
                outlet_category.visible = visible
                outlet_category.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})
    
@csrf_exempt
def update_category(request):
    if request.method == 'PUT':
        is_valid, errors = ValidatorForms.category_put_validator(request.PUT)
        if is_valid:
            category_id = request.PUT.get('id')
            category = get_object_or_404(VariantCategories, id=category_id)
            name = request.PUT.get('name')
            visible = request.PUT.get('visible')
            image = request.PUT.get('image')
            # Update the category fields here
            if name:
                category.name = name
            if visible:
                category.visible = visible
            if image:
                category.image = image
            category.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only PUT requests allowed'})

@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        is_valid, errors = ValidatorForms.category_post_validator(request.POST)
        if is_valid:
            brand_id = request.POST.get('brand_id')
            name = request.POST.get('name')
            image = request.POST.get('image')
            # Create the category here
            category = VariantCategories.objects.create(brand_id=brand_id, name=name, image=image)
            return JsonResponse({'status': 'success', 'category_id': category.id})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})

@csrf_exempt
def delete_category(request):
    if request.method == 'DELETE':
        is_valid, errors = ValidatorForms.delete_validator(request.DELETE)
        if is_valid:
            category_id = request.DELETE.get('id')
            category = get_object_or_404(VariantCategories, id=category_id)
            # Delete the category here
            category.delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only DELETE requests allowed'})
    
@csrf_exempt
def get_variants(request):
    if request.method == 'GET':
        is_valid, errors = ValidatorForms.variant_get_validator(request.GET)
        if is_valid:
            brand_id = request.GET.get('brand_id')
            order = request.GET.get('order')
            count = request.GET.get('count')
            offset = request.GET.get('offset')
            variant_categories_id = request.GET.get('variant_categories_id')

            # Fetch variants based on the form data
            variants = Variants.objects.filter(brand_id=brand_id)

            if variant_categories_id:
                variants = variants.filter(variant_categories_id=variant_categories_id)

            if order == 'desc':
                variants = variants.order_by('-id')
            else:
                variants = variants.order_by('id')

            total_count = variants.count()

            if count is not None and offset is not None:
                variants = variants[offset:offset + count]

            # Prepare the data to return as JSON response
            result = []
            for variant in variants:
                result.append({
                    'id': variant.id,
                    'name': variant.name,
                    'image': variant.image,
                    # Include other fields you want to return in the response
                })

            return JsonResponse({
                'status': 'success',
                'variants': result,
                'total_count': total_count
            })
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only GET requests allowed'})

@csrf_exempt
def create_variant(request):
    if request.method == 'POST':
        is_valid, errors = ValidatorForms.variant_post_validator(request.POST)
        if is_valid:
            variant_category_id = request.POST.get('variant_categories_id')
            name = request.POST.get('name')
            image = request.POST.get('image')
            # Create the variant here
            variant = Variants.objects.create(variant_categories_id=variant_category_id, name=name, image=image)
            return JsonResponse({'status': 'success', 'variant_id': variant.id})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})

@csrf_exempt
def update_variant(request):
    if request.method == 'PUT':
        is_valid, errors = ValidatorForms.variant_put_validator(request.PUT)
        if is_valid:
            variant_id = request.PUT.get('variant_id')
            variant = get_object_or_404(Variants, id=variant_id)
            name = request.PUT.get('name')
            visible = request.PUT.get('visible')
            image = request.PUT.get('image')
            # Update the variant fields here
            if name:
                variant.name = name
            if visible:
                variant.visible = visible
            if image:
                variant.image = image
            variant.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only PUT requests allowed'})

@csrf_exempt
def delete_variant(request):
    if request.method == 'DELETE':
        is_valid, errors = ValidatorForms.delete_validator(request.DELETE)
        if is_valid:
            variant_id = request.DELETE.get('id')
            variant = get_object_or_404(Variants, id=variant_id)
            # Delete the variant here
            variant.delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only DELETE requests allowed'})
    
@csrf_exempt
def variant_outlet_link_view(request):
    if request.method == 'POST':
        is_valid, errors = ValidatorForms.update_outlet_validator(request.POST)
        if is_valid:
            # Process the valid form data and perform actions
            data = request.POST.get('data')
            visible = request.POST.get('visible')
            outlets = request.POST.get('outlets')

            # Perform the necessary actions with the data
            # For example, you can save the data to the VariantOuletLink model
            variant_outlet_link = VariantOuletLink.objects.create(
                outlet_id=data['id'],
                visible=visible,
                variant_id=data['variant_id'],
                price=data['price'],
                sold_out=data['sold_out']
            )
            
            # Save the many-to-many field outlets
            variant_outlet_link.outlets.set(outlets)

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})