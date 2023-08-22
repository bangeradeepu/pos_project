from .models import Items, ComboItemsLink, ItemVariantLink, ItemAddonLink, Variants

async def validate_items(data, outlet_id, coupon_data=None):
    valid_items = []
    items_total = 0
    items_valid_for_discount = []
    items_total_for_discount = 0
    category_ids = set()

    for item in data['items']:
        current_item_total = 0
        addons_total = 0

        try:
            item_details = Items.objects.get(id=item['item_id'], deleted=False)
        except Items.DoesNotExist:
            raise Exception('Item does not exist')

        # Add your custom function to check if item is sold out for the given outlet_id
        is_item_sold_out(outlet_id, item)

        # Combo Check
        if item_details.item_type == 'COMBO':
            combo_items = ComboItemsLink.objects.filter(combo_id=item['item_id'])
            for combo_item in combo_items:
                # Add your custom function to check if combo item is sold out for the given outlet_id
                is_item_sold_out(outlet_id, combo_item)

        # Variant Check
        item_variant_data = None
        if item_details.item_type == 'VARIANT':
            if 'variant_id' not in item:
                raise Exception(f'"item_id" {item["item_id"]} needs a variant_id')
            try:
                item_variant_data = ItemVariantLink.objects.get(item_id=item['item_id'], variant_id=item['variant_id'])
            except ItemVariantLink.DoesNotExist:
                raise Exception(f'"item_id" {item["item_id"]}. Item variant doesn\'t exist.')

            # Add your custom function to get variant details
            variant_details = get_variant_details(item['variant_id'])
            # Add your custom function to get variant outlet data
            variant_outlet_data = get_variant_outlet_data(outlet_id, item_variant_data.id)

            if variant_outlet_data.sold_out:
                raise Exception(f'Variant, "variant_id" {item["variant_id"]} of "item_id" {item["item_id"]} is sold out')

            item_variant_data.name = variant_details.name
            item_variant_data.price = variant_outlet_data.price
            current_item_total += item['quantity'] * variant_outlet_data.price
        else:
            if 'variant_id' in item:
                raise Exception(f'"item_id" {item["item_id"]} cannot have a variant_id')
            current_item_total += item['quantity'] * item_details.price

        # Addon Check
        item_addons_list = []
        if 'addon_variants' in item:
            for addon in item['addon_variants']:
                try:
                    item_addon_link_data = ItemAddonLink.objects.get(item_id=item['item_id'], addon_variant_id=addon)
                except ItemAddonLink.DoesNotExist:
                    raise Exception(f'"item_id" {item["item_id"]}, "addon_id" {addon}. This addon is not available for this item')

                # Add your custom function to get addon variant outlet data
                item_addon_outlet_data = get_addon_variant_outlet_data(outlet_id, addon)

                if item_addon_outlet_data.sold_out:
                    raise Exception(f'"item_id" {item["item_id"]}, "addon_id" {addon}. This addon is sold out')

                # Add your custom function to get addon variant details
                item_addon_details = get_addon_variant_details(addon)
                item_addons_list.append(item_addon_details)
                addons_total += item['quantity'] * item_addon_details.price
                current_item_total += addons_total

        if coupon_data:
            if item_details.category_id not in coupon_data.excluded_categories:
                items_total_for_discount += current_item_total
                items_valid_for_discount.append(item['id'])

        items_total += current_item_total

        valid_items.append({
            'id': item['id'],
            'category_id': item_details.category_id,
            'item_id': item['item_id'],
            'item_name': item_details.name,
            'quantity': item['quantity'],
            'price': item_variant_data.price if item_variant_data else item_details.price,
            'item_variant_name': item_variant_data.name if item_variant_data else '',
            'item_variant_id': item_variant_data.id if item_variant_data else None,
            'addon_variants': item_addons_list,
            'addons_total': addons_total,
            'total': current_item_total,
        })
        category_ids.add(item_details.category_id)

    return {
        'items': valid_items,
        'itemsValidForDiscount': items_valid_for_discount,
        'total': items_total,
        'totalForDiscount': items_total_for_discount,
        'categories': list(category_ids),
    }
