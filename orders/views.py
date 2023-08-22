from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Orders,Reviews,OrderItems
from .validations import (
    DeleteValidatorForm, 
    PostValidationForm, 
    PutValidationForm,
    OrderItemsForm,
    OrdersEditedForm, 
    OrderTimelineForm,
    OrderOnlinePaymentForm,
    get_validator,
    post_validation,
)
from django.core.exceptions import ValidationError
import json 

# View to update an order
@require_http_methods(['PUT'])
def update_order(request):
    form = PutValidationForm(request.PUT)
    if form.is_valid():
        # Extract the data from the form
        data = form.cleaned_data

        order_id = data['order_id']
        update_type = data['update_type']

        # Assuming you have a model manager named 'orders_manager'
        order = get_object_or_404(Orders, id=order_id)

        if update_type == 'DETAILS_UPDATE':
            # Update order details based on the form data
            name = data['data']['name']
            address_id = data['data']['address_id']
            note = data['data']['note']
            alternate_phone = data['data']['alternate_phone']
            contactless = data['data']['contactless']
            third_party_service_type = data['data']['third_party_service_type']
            payment_mode = data['data']['payment_mode']
            order_type = data['data']['order_type']
            order_time = data['data']['order_time']
            pre_order_time = data['data'].get('pre_order_time')
            coupon_id = data['data']['coupon_id']

            # Update the order model fields accordingly
            order.name = name
            order.address_id = address_id
            order.note = note
            order.alternate_phone = alternate_phone
            order.contactless = contactless
            order.third_party_service_type = third_party_service_type
            order.payment_mode = payment_mode
            order.order_type = order_type
            order.order_time = order_time
            order.pre_order_time = pre_order_time
            order.coupon_id = coupon_id

        elif update_type == 'DE_UPDATE':
            # Update DE details based on the form data
            de_id = data['data']['de_id']

            # Update the order model fields accordingly
            order.de_id = de_id

        elif update_type == 'STATUS_UPDATE':
            # Update order status based on the form data
            status = data['data']['status']

            # Update the order model fields accordingly
            order.order_status = status

        elif update_type == 'ITEMS_UPDATE':
            # Update items based on the form data
            items = data['data']
            for item_data in items:
                item_id = item_data['item_id']
                quantity = item_data['quantity']
                variant_id = item_data.get('variant_id')
                addon_variants = item_data.get('addon_variants')

                # Assuming you have a related model for items and addons
                # You can update the related models here

        # Save the order after updates
        order.save()

        return JsonResponse({'message': 'Order updated successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

@require_http_methods(['GET'])
def get_order(request, order_id):
    try:
        order = Orders.objects.get(order_id=order_id)
        order_data = {
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'customer_id': order.customer_id,
            'order_status': order.order_status,
            'epoch_time': order.epoch_time,
            'created_on': order.created_on,
            'modified_on': order.modified_on,
            'pre_order_time': order.pre_order_time,
            'de_id': order.de_id,
            'location': order.location,
            'delivery_type_id': order.delivery_type_id,
            'note': order.note,
            'phone': order.phone,
            'alternate_phone': order.alternate_phone,
            'address_id': order.address_id,
            'coupon_id': order.coupon_id,
            'coupon_details': order.coupon_details,
            'total': order.total,
            'tip': order.tip,
            'additional_charges': order.additional_charges,
            'contactless': order.contactless,
            'cancel_reason': order.cancel_reason,
            'platform_details': order.platform_details,
            'visible': order.visible,
            'payment_mode': order.payment_mode,
            'payment_status': order.payment_status,
            'invoice_id': order.invoice_id,
            'third_party_service_id': order.third_party_service_id,
            'third_party_service_type': order.third_party_service_type,
            'order_type': order.order_type,
        }
        return JsonResponse({'message': 'Order details retrieved successfully', 'data': order_data})
    except Orders.DoesNotExist:
        return JsonResponse({'message': 'Order not found'}, status=404)


# View to create an order
@require_http_methods(['POST'])
def create_order(request):
    form = PostValidationForm(request.POST)
    if form.is_valid():
        # Extract the data from the form
        data = form.cleaned_data

        # Assuming you have a model manager named 'orders_manager'
        order = Orders.objects.create(
            order_id=data['order_id'],
            customer_name=data['customer_name'],
            customer_id=data['customer_id'],
            order_status=data['order_status'],
            epoch_time=data['epoch_time'],
            created_on=data['created_on'],
            modified_on=data['modified_on'],
            pre_order_time=data['pre_order_time'],
            de_id=data['de_id'],
            location=data['location'],
            delivery_type_id=data['delivery_type_id'],
            note=data['note'],
            phone=data['phone'],
            alternate_phone=data['alternate_phone'],
            address_id=data['address_id'],
            coupon_id=data['coupon_id'],
            coupon_details=data['coupon_details'],
            total=data['total'],
            tip=data['tip'],
            additional_charges=data['additional_charges'],
            contactless=data['contactless'],
            cancel_reason=data['cancel_reason'],
            platform_details=data['platform_details'],
            visible=data['visible'],
            payment_mode=data['payment_mode'],
            payment_status=data['payment_status'],
            invoice_id=data['invoice_id'],
            third_party_service_id=data['third_party_service_id'],
            third_party_service_type=data['third_party_service_type'],
            order_type=data['order_type'],
        )

        return JsonResponse({'message': 'Order created successfully', 'data': {'id': order.id}})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

# View to delete an order
@require_http_methods(['DELETE'])
def delete_order(request):
    form = DeleteValidatorForm(request.DELETE)
    if form.is_valid():
        order_id = form.cleaned_data['id']
        # Use get_object_or_404 if you want to handle non-existing records gracefully
        order = get_object_or_404(Orders, id=order_id)
        order.delete()
        return JsonResponse({'message': 'Order deleted successfully'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)



def get_order_item(request, order_item_id):
    if request.method == 'GET':
        try:
            order_item = OrderItems.objects.get(pk=order_item_id)
            item_data = {
                'id': order_item.id,
                'order_id': order_item.order_id,
                'item_id': order_item.item_id,
                'quantity': order_item.quantity,
                'price': order_item.price,
                'item_variant_name': order_item.item_variant_name,
                'addon_variants': order_item.addon_variants,
                'addons_total': order_item.addons_total,
                'total': order_item.total,
                'brand_id': order_item.brand_id,
            }
            return JsonResponse({'status': 'success', 'data': item_data})
        except OrderItems.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Order item not found'}, status=404)
    else:
        return HttpResponseNotAllowed(['GET'])

def create_order_item(request):
    if request.method == 'POST':
        form = OrderItemsForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            order_item = form.save()
            return JsonResponse({'status': 'success', 'message': 'Order item created successfully', 'id': order_item.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = OrderItemsForm()

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
 
def delete_order_item(request, order_item_id):
    if request.method == 'DELETE':
        try:
            order_item = OrderItems.objects.get(pk=order_item_id)
            order_item.delete()
            return JsonResponse({'status': 'success', 'message': 'Order item deleted successfully'})
        except OrderItems.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Order item not found'}, status=404)
    else:
        return HttpResponseNotAllowed(['DELETE'])
 


def create_orders_edited(request):
    if request.method == 'POST':
        form = OrdersEditedForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            orders_edited = form.save()
            return JsonResponse({'status': 'success', 'message': 'Orders edited created successfully', 'id': orders_edited.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def create_order_timeline(request):
    if request.method == 'POST':
        form = OrderTimelineForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            order_timeline = form.save()
            return JsonResponse({'status': 'success', 'message': 'Order timeline created successfully', 'id': order_timeline.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def create_order_online_payment(request):
    if request.method == 'POST':
        form = OrderOnlinePaymentForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            order_online_payment = form.save()
            return JsonResponse({'status': 'success', 'message': 'Order online payment created successfully', 'id': order_online_payment.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@require_http_methods(['GET'])
def get_reviews(request):
    data = request.GET.dict()
    validation_result = get_validator(data)

    if validation_result.error:
        errors = [error.message for error in validation_result.error.details]
        return JsonResponse({'errors': errors}, status=400)

    # Query the database based on the validated data and return the reviews
    reviews = Reviews.objects.filter(order_id=data.get('order_id'), type=data.get('order'))

    return JsonResponse({'reviews': list(reviews.values())})

@require_http_methods(['POST'])
def create_review(request):
    data = json.loads(request.body)
    validation_result = post_validation(data)

    if validation_result.error:
        errors = [error.message for error in validation_result.error.details]
        return JsonResponse({'errors': errors}, status=400)

    try:
        review = Reviews(
            order_id=data['order_id'],
            type=data['type'],
            type_id=data['type_id'],
            stars=data['stars'],
            review=data['review'],
            photos=data['photos'],
            created_on=data['created_on']
        )
        review.save()
        return JsonResponse({'message': 'Review created successfully', 'data': review.id})
    except ValidationError as e:
        return JsonResponse({'errors': e.messages}, status=400)
