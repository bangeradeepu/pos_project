from rest_framework import generics
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from .models import AddonCategories, AddonVariants, AddonCategoryOutletLink, AddonVariantOutletLink
from .serializers import AddonCategoriesSerializer, AddonVariantsSerializer
from .validations import (
    get_validator, addon_get_validator, category_post_validator,
    category_put_validator, delete_validator, update_outlet_validator,
    addon_post_validator, addon_put_validator, addon_category_link_validator
)

def category_post_view(request):
    try:
        category_post_validator(request.POST)  # Validate the POST request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    brand_id = request.POST.get('brand_id')
    name = request.POST.get('name')
    image = request.POST.get('image')

    # Now, you can use the 'brand_id', 'name', and 'image' variables to create a new category in your database or perform any other operation.

    # For example, you might create a new category using a serializer if you are using Django Rest Framework:
    category_data = {'brand_id': brand_id, 'name': name, 'image': image}
    serializer = AddonCategoriesSerializer(data=category_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def category_get_view(request):
    try:
        get_validator(request.GET)  # Validate the GET request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    order = request.GET.get('order')
    count = request.GET.get('count')
    offset = request.GET.get('offset')
    brand_id = request.GET.get('brand_id')

    # Now, you can use the 'order', 'count', 'offset', and 'brand_id' variables to perform any filtering or retrieval of data from the database based on the query parameters.

    # For example, you might retrieve a list of categories based on the query parameters using Django's ORM:
    categories = AddonCategories.objects.filter(brand_id=brand_id)

    # Apply any additional filtering based on the 'order', 'count', and 'offset' if required.
    if order:
        if order == 'asc':
            categories = categories.order_by('name')
        elif order == 'desc':
            categories = categories.order_by('-name')

    if count:
        try:
            count = int(count)
            categories = categories[:count]
        except ValueError:
            pass

    if offset:
        try:
            offset = int(offset)
            categories = categories[offset:]
        except ValueError:
            pass

    # Now, serialize the list of categories and return the JSON response.
    serializer = AddonCategoriesSerializer(categories, many=True)
    return JsonResponse(serializer.data, status=200)

def addon_get_view(request):
    try:
        addon_get_validator(request.GET)  # Validate the GET request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    order = request.GET.get('order')
    count = request.GET.get('count')
    offset = request.GET.get('offset')
    addon_categories_id = request.GET.get('addon_categories_id')

    # Now, you can use the 'order', 'count', 'offset', and 'addon_categories_id' variables to perform any filtering or retrieval of data from the database based on the query parameters.

    # For example, you might retrieve a list of addons based on the query parameters using Django's ORM:
    addons = AddonVariants.objects.filter(addon_categories_id=addon_categories_id)

    # Apply any additional filtering based on the 'order', 'count', and 'offset' if required.
    if order:
        if order == 'asc':
            addons = addons.order_by('name')
        elif order == 'desc':
            addons = addons.order_by('-name')

    if count:
        try:
            count = int(count)
            addons = addons[:count]
        except ValueError:
            pass

    if offset:
        try:
            offset = int(offset)
            addons = addons[offset:]
        except ValueError:
            pass

    # Now, serialize the list of addons and return the JSON response.
    serializer = AddonVariantsSerializer(addons, many=True)
    return JsonResponse(serializer.data, status=200)

def category_put_view(request):
    try:
        category_put_validator(request.POST)  # Validate the PUT request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    category_id = request.POST.get('id')  # Assuming the 'id' is provided in the request data
    name = request.POST.get('name')
    visible = request.POST.get('visible')
    image = request.POST.get('image')

    try:
        category = AddonCategories.objects.get(pk=category_id)  # Assuming 'AddonCategories' is the model representing the category data
    except AddonCategories.DoesNotExist:
        return JsonResponse({"error": "Category not found."}, status=404)

    # Update the category object with the new data
    if name:
        category.name = name
    if visible is not None:
        category.visible = bool(visible)
    if image:
        category.image = image

    # Save the updated category object
    category.save()

    # Now, you can return a JSON response indicating the successful update
    serializer = AddonCategoriesSerializer(category)  # Assuming 'AddonCategoriesSerializer' is the serializer for the 'AddonCategories' model
    return JsonResponse(serializer.data, status=200)

def delete_view(request):
    try:
        delete_validator(request.POST)  # Validate the DELETE request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    category_id = request.POST.get('id')  # Assuming the 'id' of the category to be deleted is provided in the request data

    try:
        category = AddonCategories.objects.get(pk=category_id)  # Assuming 'AddonCategories' is the model representing the category data
    except AddonCategories.DoesNotExist:
        return JsonResponse({"error": "Category not found."}, status=404)

    # If the category exists, delete it from the database
    category.delete()

    # Now, you can return a JSON response indicating the successful deletion
    return JsonResponse({"message": "Category deleted successfully."}, status=200)

def addon_put_view(request):
    try:
        addon_put_validator(request.POST)  # Validate the PUT request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    # ... Implement the logic for updating the addon based on the valid request data
    # For example, you can retrieve the addon ID, name, price, visibility, etc., from the request data
    addon_id = request.POST.get('addon_id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    visibility = request.POST.get('visible')
    # Retrieve other properties as needed...

    # Now you can use the retrieved data to update the addon in your database
    try:
        addon = AddonVariants.objects.get(pk=addon_id)
        addon.name = name
        addon.price = price
        addon.visible = visibility
        # Update other properties as needed...
        addon.save()

        # If everything went well, you can return a success response
        return JsonResponse({"message": "Addon updated successfully."}, status=200)
    except AddonVariants.DoesNotExist:
        # If the addon with the specified ID doesn't exist, return a not found error
        return JsonResponse({"error": "Addon not found."}, status=404)
    except Exception as e:
        # Handle any other exceptions that might occur during the update process
        return JsonResponse({"error": str(e)}, status=500)

def addon_post_view(request):
    try:
        addon_post_validator(request.POST)  # Validate the POST request
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    # If the request data is valid, proceed with further operations
    # ... Implement the logic for creating a new addon based on the valid request data
    # For example, you can retrieve the addon name, price, addon_categories_id, food_tag, image, etc., from the request data
    name = request.POST.get('name')
    price = request.POST.get('price')
    addon_categories_id = request.POST.get('addon_categories_id')
    food_tag = request.POST.get('food_tag')
    image = request.POST.get('image')
    # Retrieve other properties as needed...

    # Now you can use the retrieved data to create a new addon in your database
    try:
        addon = AddonVariants.objects.create(
            name=name,
            price=price,
            addon_categories_id=addon_categories_id,
            food_tag=food_tag,
            image=image,
            # Set other properties as needed...
        )

        # If everything went well, you can return a success response with the new addon details
        serializer = AddonVariantsSerializer(addon)  # Assuming you have a serializer for AddonVariants model
        return JsonResponse(serializer.data, status=201)
    except Exception as e:
        # Handle any exceptions that might occur during the addon creation process
        return JsonResponse({"error": str(e)}, status=500)

class UpdateOutletView(APIView):
    def put(self, request):
        try:
            # Call the validator to validate the PUT request data
            update_outlet_validator(request.data)
        except ValidationError as e:
            # If the validation fails, return a JSON response with the error message
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # If the request data is valid, proceed with further operations
        # ... Implement the logic for updating the outlet based on the valid request data
        # For example, you can retrieve the outlet ID, name, address, contact information, etc., from the request data
        outlet_id = request.data.get('outlet_id')
        name = request.data.get('name')
        address = request.data.get('address')
        contact_info = request.data.get('contact_info')
        # Retrieve other properties as needed...

        # Now you can use the retrieved data to update the outlet in your database
        try:
            outlet = AddonVariantOutletLink.objects.get(pk=outlet_id)
            outlet.name = name
            outlet.address = address
            outlet.contact_info = contact_info
            # Update other properties as needed...
            outlet.save()

            # If everything went well, you can return a success response
            return Response({"message": "Outlet updated successfully."}, status=status.HTTP_200_OK)
        except AddonVariantOutletLink.DoesNotExist:
            # If the outlet with the specified ID doesn't exist, return a not found error
            return Response({"error": "Outlet not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle any other exceptions that might occur during the update process
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@csrf_exempt 
def create_addon_category_link(request):
    if request.method == 'POST':
        outlet_id = request.POST.get('outlet_id')
        addon_categories_id = request.POST.get('addon_categories_id')
        visible = request.POST.get('visible', True)
        
        # Validate the data before creating the object
        data = {
            'outlet_id': int(outlet_id),
            'addon_categories_id': int(addon_categories_id),
            'visible': bool(visible),
        }
        try:
            addon_category_link_validator(data)
        except ValidationError as e:
            error_message = e.message
            return JsonResponse({'error': error_message}, status=400)
        
        # Data is valid, create the object
        addon_category_link = AddonCategoryOutletLink(
            outlet_id=outlet_id,
            addon_categories_id=addon_categories_id,
            visible=visible,
        )
        addon_category_link.save()
        
        return JsonResponse({'message': 'Add-on category link created successfully'})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
