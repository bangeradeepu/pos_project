from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import ItemVariantLink, ComboItemsLink, Items, ItemOutletLink, ItemAddonLink
from .validations import (
    ComboValidatorForm, 
    ComboDeleteValidatorForm, 
    GetValidatorForm,
    PostValidatorForm,
    PutValidatorForm,
    DeleteValidatorForm,
    VariantPostValidatorForm, 
    VariantPutValidatorForm, 
    VariantDeleteValidatorForm,
    UpdateOutletValidatorForm,
    AddonsPostValidatorForm,
)

# View to validate and create ComboItemsLink
@require_http_methods(['POST'])
def create_combo_items_link(request):
    form = ComboValidatorForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data['id']
        combos = form.cleaned_data['combos']

        # Assuming you have a model manager named 'combo_items_link_manager'
        combo_items_link_manager = ComboItemsLink.objects
        for combo in combos:
            item_id = combo['item_id']
            qty = combo['qty']
            combo_items_link_manager.create(combo_id=id, item_id=item_id, qty=qty)

        return JsonResponse({'message': 'Combo items created successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

# View to validate and delete ComboItemsLink
@require_http_methods(['POST'])
def delete_combo_items_link(request):
    form = ComboDeleteValidatorForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data['id']
        combos = form.cleaned_data['combos']

        # Assuming you have a model manager named 'combo_items_link_manager'
        combo_items_link_manager = ComboItemsLink.objects
        for combo in combos:
            item_id = combo['item_id']
            # Use get_object_or_404 if you want to handle non-existing records gracefully
            combo_item = get_object_or_404(combo_items_link_manager, combo_id=id, item_id=item_id)
            combo_item.delete()

        return JsonResponse({'message': 'Combo items deleted successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
    
def get_view(request):
    form = GetValidatorForm(request.GET)
    if form.is_valid():
        order = form.cleaned_data.get('order', None)
        count = form.cleaned_data.get('count', None)
        offset = form.cleaned_data.get('offset', None)

        # Assuming you have a model manager named 'items_manager'
        items_manager = Items.objects

        # Apply filters based on valid form data
        items = items_manager.all()
        if order:
            items = items.order_by(order)
        if count:
            items = items[:count]
        if offset:
            items = items[offset:]

        # Serialize the items to JSON format (if needed) and return the response
        serialized_items = []
        for item in items:
            serialized_item = {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'category_id': item.category_id,
                'food_tag': item.food_tag,
                'price': str(item.price),  # Convert DecimalField to string
                'media_url': item.media_url,
                'item_type': item.item_type,
            }
            serialized_items.append(serialized_item)

        return JsonResponse({'data': serialized_items})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

def post_view(request):
    form = PostValidatorForm(request.POST)
    if form.is_valid():
        # Get cleaned and validated data from the form
        cleaned_data = form.cleaned_data

        # Assuming you have a model manager named 'items_manager'
        items_manager = items_manager.objects

        # Perform additional processing or validations before saving the item
        # For example, you can check if the item already exists with the same name
        if items_manager.filter(name=cleaned_data['name']).exists():
            return JsonResponse({'errors': {'name': ['An item with this name already exists.']}}, status=400)

        # Save the new item to the database using the form data
        item = form.save()

        # Return the created item data as a JSON response
        return JsonResponse({'message': 'Item created successfully', 'data': {'id': item.id}})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

def put_view(request):
    form = PutValidatorForm(request.PUT, instance=Items())
    if form.is_valid():
        # Get cleaned and validated data from the form
        cleaned_data = form.cleaned_data

        # Assuming you have a model manager named 'items_manager'
        items_manager = Items.objects

        try:
            # Get the existing item with the specified ID
            item_id = cleaned_data['id']
            item = items_manager.get(id=item_id)

            # Update the item with the new data
            for field, value in cleaned_data.items():
                setattr(item, field, value)

            # Save the updated item to the database
            item.save()

            # Return the updated item data as a JSON response
            return JsonResponse({'message': 'Item updated successfully', 'data': {'id': item.id}})
        except Items.DoesNotExist:
            return JsonResponse({'errors': {'id': ['Item with the specified ID does not exist.']}}, status=404)
    else:
        return JsonResponse({'errors': form.errors}, status=400)

def delete_view(request):
    form = DeleteValidatorForm(request.DELETE)
    if form.is_valid():
        id = form.cleaned_data['id']
        try:
            item = Items.objects.get(id=id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'})
        except Items.DoesNotExist:
            return JsonResponse({'errors': {'id': ['Item with the specified id does not exist.']}}, status=404)
    else:
        return JsonResponse({'errors': form.errors}, status=400)
    


@require_http_methods(['POST'])
def variant_post_view(request):
    form = VariantPostValidatorForm(request.POST)
    if form.is_valid():
        item_id = form.cleaned_data['id']
        variants = form.cleaned_data['variants']

        # Assuming you have a model manager named 'item_variant_link_manager'
        item_variant_link_manager = ItemVariantLink.objects
        for variant_data in variants:
            variant_id = variant_data['variant_id']
            price = variant_data['price']
            item_variant_link_manager.create(item_id=item_id, variant_id=variant_id)

        return JsonResponse({'message': 'Variant items linked successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

@require_http_methods(['PUT'])
def variant_put_view(request):
    form = VariantPutValidatorForm(request.PUT)
    if form.is_valid():
        variant_data_list = form.cleaned_data['variant_data']

        # Assuming you have a model manager named 'item_variant_link_manager'
        item_variant_link_manager = ItemVariantLink.objects
        for variant_data in variant_data_list:
            item_variant_id = variant_data['item_variant']['id']
            price = variant_data['item_variant'].get('price')
            visible = variant_data['item_variant'].get('visible')
            sold_out = variant_data['item_variant'].get('sold_out')

            # Use get_object_or_404 if you want to handle non-existing records gracefully
            item_variant = get_object_or_404(item_variant_link_manager, id=item_variant_id)
            if price is not None:
                item_variant.price = price
            if visible is not None:
                item_variant.visible = visible
            if sold_out is not None:
                item_variant.sold_out = sold_out
            item_variant.save()

        return JsonResponse({'message': 'Variant items updated successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

@require_http_methods(['DELETE'])
def variant_delete_view(request):
    form = VariantDeleteValidatorForm(request.DELETE)
    if form.is_valid():
        item_id = form.cleaned_data['id']
        variants = form.cleaned_data['variants']

        # Assuming you have a model manager named 'item_variant_link_manager'
        item_variant_link_manager = ItemVariantLink.objects
        for variant_id in variants:
            # Use get_object_or_404 if you want to handle non-existing records gracefully
            item_variant = get_object_or_404(item_variant_link_manager, item_id=item_id, variant_id=variant_id)
            item_variant.delete()

        return JsonResponse({'message': 'Variant items unlinked successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)


@require_http_methods(['POST'])
def create_item_outlet_link(request):
    form = UpdateOutletValidatorForm(request.POST)
    
    if form.is_valid():
        outlet_data_list = form.cleaned_data['outlet_data']
        item_outlet_link_manager = ItemOutletLink.objects
        
        for outlet_data in outlet_data_list:
            item_id = outlet_data['data']['item_id']
            outlet_id_list = outlet_data['outlets']
            
            for outlet_id in outlet_id_list:
                # Extract data
                price = outlet_data['data'].get('price')
                visible = outlet_data['data'].get('visible')
                sold_out = outlet_data['data'].get('sold_out')
                rank = outlet_data['data'].get('rank')
                
                # Get or create the item outlet link
                item_outlet_link, created = item_outlet_link_manager.get_or_create(item_id=item_id, outlet_id=outlet_id)
                
                # Update fields
                item_outlet_link.price = price
                item_outlet_link.visible = visible
                item_outlet_link.sold_out = sold_out
                item_outlet_link.rank = rank
                item_outlet_link.unit = outlet_data['data'].get('unit', '')
                item_outlet_link.tag = outlet_data['data'].get('tag', '')
                item_outlet_link.strike_price = outlet_data['data'].get('strike_price', 0)
                
                item_outlet_link.save()
        
        return JsonResponse({'message': 'Item outlet links created successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

@require_http_methods(['PUT'])
def update_item_outlet_link(request):
    form = UpdateOutletValidatorForm(request.data)
    
    if form.is_valid():
        outlet_data_list = form.cleaned_data['outlet_data']
        item_outlet_link_manager = ItemOutletLink.objects
        
        for outlet_data in outlet_data_list:
            item_id = outlet_data['data']['item_id']
            outlet_id_list = outlet_data['outlets']
            
            for outlet_id in outlet_id_list:
                # Extract data
                price = outlet_data['data'].get('price')
                visible = outlet_data['data'].get('visible')
                sold_out = outlet_data['data'].get('sold_out')
                rank = outlet_data['data'].get('rank')
                
                # Get or create the item outlet link
                item_outlet_link, created = item_outlet_link_manager.get_or_create(item_id=item_id, outlet_id=outlet_id)
                
                # Update fields
                item_outlet_link.price = price
                item_outlet_link.visible = visible
                item_outlet_link.sold_out = sold_out
                item_outlet_link.rank = rank
                item_outlet_link.unit = outlet_data['data'].get('unit', '')
                item_outlet_link.tag = outlet_data['data'].get('tag', '')
                item_outlet_link.strike_price = outlet_data['data'].get('strike_price', 0)
                
                item_outlet_link.save()
        
        return JsonResponse({'message': 'Item outlet links updated successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
# View to validate and create ItemAddonLink
@require_http_methods(['POST'])
def create_item_addon_link(request):
    form = AddonsPostValidatorForm(request.POST)
    if form.is_valid():
        item_id = form.cleaned_data['id']
        addon_ids = form.cleaned_data['addons']

        # Assuming you have a model manager named 'item_addon_link_manager'
        item_addon_link_manager = ItemAddonLink.objects
        for addon_id in addon_ids:
            item_addon_link_manager.create(item_id=item_id, addon_variant_id=addon_id)

        return JsonResponse({'message': 'Item addon links created successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
