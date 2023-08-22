from rest_framework import generics
from .models import Categories, CategoryOutletLink
from .serializers import CategoriesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .validations import RouteValidator


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def categories_view(request):
    if request.method == 'GET':
        data = request.query_params.dict()
        validated_data = RouteValidator.get_validator(data)
        # Process the validated_data
        # Query the Categories model based on the validated data
        categories = Categories.objects.filter(
            brand_id=validated_data.get('brand_id'),
            visible=validated_data.get('visible', False),
        )
        # You can further filter and process the data based on other validated fields if needed
        # For example: order, count, offset
        
        # Serialize the queryset and return the response
        # Assuming you have a serializer for the Categories model
        # Replace 'YourCategoriesSerializer' with the actual serializer class
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        validated_data = RouteValidator.post_validator(data)
        # Process the validated_data
        # Create a new Categories object based on the validated data
        category = Categories.objects.create(
            name=validated_data.get('name'),
            display_in=validated_data.get('display_in'),
            image=validated_data.get('image'),
            visible=validated_data.get('visible', False),
            brand_id=validated_data.get('brand_id'),
            mrp_items=validated_data.get('mrp_items', False),
            single_unavailable=validated_data.get('single_unavailable', False),
        )
        # You can further process the data or perform any other actions based on your requirements
        
        # Return a success response indicating the object was created
        return Response({"message": "Category created successfully.", "id": category.id})

    elif request.method == 'PUT':
        data = request.data
        validated_data = RouteValidator.put_validator(data)
        # Process the validated_data
        # Update an existing Categories object based on the validated data
        category_id = validated_data.get('id')
        try:
            category = Categories.objects.get(pk=category_id)
        except Categories.DoesNotExist:
            return Response({"message": "Category not found."}, status=404)

        category.name = validated_data.get('name', category.name)
        category.display_in = validated_data.get('display_in', category.display_in)
        category.image = validated_data.get('image', category.image)
        category.visible = validated_data.get('visible', category.visible)
        category.brand_id = validated_data.get('brand_id', category.brand_id)
        category.mrp_items = validated_data.get('mrp_items', category.mrp_items)
        category.single_unavailable = validated_data.get('single_unavailable', category.single_unavailable)
        category.save()
        # You can further process the data or perform any other actions based on your requirements
        
        # Return a success response indicating the object was updated
        return Response({"message": "Category updated successfully."})

    elif request.method == 'DELETE':
        data = request.data
        validated_data = RouteValidator.delete_validator(data)
        # Process the validated_data
        category_id = validated_data.get('id')
        try:
            category = Categories.objects.get(pk=category_id)
        except Categories.DoesNotExist:
            return Response({"message": "Category not found."}, status=404)

        # Perform the delete action
        category.delete()
        # You can further process the data or perform any other actions based on your requirements
        
        # Return a success response indicating the object was deleted
        return Response({"message": "Category deleted successfully."})

@api_view(['PUT'])
def update_outlet_categories_view(request):
    data = request.data
    validated_data = RouteValidator.update_outlet_validator(data)
    # Process the validated_data
    for item in validated_data:
        category_data = item.get('data')
        outlets = item.get('outlets')
        
        category_id = category_data.get('category_id')
        try:
            category = Categories.objects.get(pk=category_id)
        except Categories.DoesNotExist:
            return Response({"message": "Category not found."}, status=404)

        category.visible = category_data.get('visible', category.visible)
        category.rank = category_data.get('rank', category.rank)
        category.save()

        # Update the CategoryOutletLink model or perform any other actions based on your requirements
        # For example:
        # Update the CategoryOutletLink model to link/unlink outlets with the category
        for outlet_id in outlets:
            try:
                outlet_link = CategoryOutletLink.objects.get(outlet_id=outlet_id, category_id=category_id)
            except CategoryOutletLink.DoesNotExist:
                outlet_link = CategoryOutletLink.objects.create(
                    outlet_id=outlet_id,
                    category_id=category_id,
                    visible=category.visible,
                    rank=category.rank
                )
            outlet_link.visible = category.visible
            outlet_link.rank = category.rank
            outlet_link.save()

        # Remove any existing outlet links not present in the outlets list
        CategoryOutletLink.objects.filter(category_id=category_id).exclude(outlet_id__in=outlets).delete()

    return Response({"message": "Outlet categories updated successfully."})