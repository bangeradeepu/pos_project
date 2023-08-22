from django import forms
from customers.models import CustomerAddresses 
from .models import OrderTimeline, OrderOnlinePayment, OrderItems, OrdersEdited
from pos_project.constants import (
    PAYMENT_MODE,
    ORDER_TYPE, 
    ORDER_TIME,
    ORDER_UPDATES, 
    PAYMENT_MODE, 
    ORDER_TYPE, 
    ORDER_TIME, 
    ORDER_STATUS,
 ) 
from pos_project import constants 

class PostValidationForm(forms.Form):
    name = forms.CharField(min_length=3, required=False)
    address_id = forms.IntegerField()
    note = forms.CharField(min_length=3, required=False)
    alternate_phone = forms.CharField(min_length=10, required=False)
    tip = forms.DecimalField(min_value=0, required=False)
    contactless = forms.BooleanField(required=False)
    platform_details = forms.JSONField()
    payment_mode = forms.ChoiceField(choices=[(key, key) for key in PAYMENT_MODE.keys()])
    order_type = forms.ChoiceField(choices=[(key, key) for key in ORDER_TYPE.keys()])
    order_time = forms.ChoiceField(choices=[(key, key) for key in ORDER_TIME.keys()])
    pre_order_time = forms.IntegerField(required=False)

    def clean_address_id(self):
        address_id = self.cleaned_data['address_id']
        # Assuming Address model has a manager named 'address_manager'
        address = CustomerAddresses.address_manager.get(pk=address_id)
        if not address:
            raise forms.ValidationError('Invalid address_id')
        return address_id

    def clean_pre_order_time(self):
        order_time = self.cleaned_data.get('order_time')
        pre_order_time = self.cleaned_data.get('pre_order_time')
        if order_time == 'PRE_ORDER':
            if pre_order_time is None:
                raise forms.ValidationError('pre_order_time is required for order_time PRE_ORDER')
        else:
            if pre_order_time is not None:
                raise forms.ValidationError('pre_order_time should be provided only for order_time PRE_ORDER')
        return pre_order_time
    

class PutValidationForm(forms.Form):
    order_id = forms.IntegerField()
    update_type = forms.ChoiceField(choices=[(key, key) for key in ORDER_UPDATES.keys()])
    data = forms.JSONField()

    def clean_order_id(self):
        order_id = self.cleaned_data['order_id']
        # You can add validation logic for the order_id here if needed
        return order_id

    def clean_data(self):
        data = self.cleaned_data['data']
        update_type = self.cleaned_data.get('update_type')

        if update_type == ORDER_UPDATES.DETAILS_UPDATE:
            # Validate data for DETAILS_UPDATE
            name = data.get('name', None)
            address_id = data.get('address_id', None)
            note = data.get('note', None)
            alternate_phone = data.get('alternate_phone', None)
            contactless = data.get('contactless', None)
            third_party_service_type = data.get('third_party_service_type', None)
            payment_mode = data.get('payment_mode', None)
            order_type = data.get('order_type', None)
            order_time = data.get('order_time', None)
            pre_order_time = data.get('pre_order_time', None)
            coupon_id = data.get('coupon_id', None)

            if name is not None and len(name) < 3:
                raise forms.ValidationError('name must be at least 3 characters long')

            # Add similar validations for other fields

            # Additional validation for pre_order_time when order_time is PRE_ORDER
            if order_time == 'PRE_ORDER' and pre_order_time is None:
                raise forms.ValidationError('pre_order_time is required for order_time PRE_ORDER')
            elif order_time != 'PRE_ORDER' and pre_order_time is not None:
                raise forms.ValidationError('pre_order_time should not be provided for non-PRE_ORDER orders')

        elif update_type == ORDER_UPDATES.DE_UPDATE:
            # Validate data for DE_UPDATE
            de_id = data.get('de_id', None)
            if de_id is None:
                raise forms.ValidationError('de_id is required for DE_UPDATE')

        elif update_type == ORDER_UPDATES.STATUS_UPDATE:
            # Validate data for STATUS_UPDATE
            status = data.get('status', None)
            if status not in ORDER_STATUS.keys():
                raise forms.ValidationError('Invalid status value')

        elif update_type == ORDER_UPDATES.ITEMS_UPDATE:
            # Validate data for ITEMS_UPDATE
            items = data
            if not isinstance(items, list) or len(items) < 1:
                raise forms.ValidationError('At least one item update must be provided')
            for item in items:
                item_id = item.get('item_id', None)
                quantity = item.get('quantity', None)
                variant_id = item.get('variant_id', None)
                addon_variants = item.get('addon_variants', None)

                if item_id is None:
                    raise forms.ValidationError('item_id is required for each item update')
                if quantity is None or quantity < 1:
                    raise forms.ValidationError('quantity must be at least 1 for each item update')
                if variant_id is not None and not isinstance(variant_id, int):
                    raise forms.ValidationError('variant_id must be an integer')
                if addon_variants is not None and (not isinstance(addon_variants, list) or any(not isinstance(av, int) for av in addon_variants)):
                    raise forms.ValidationError('addon_variants must be a list of integers')

        return data
    
class DeleteValidatorForm(forms.Form):
    id = forms.IntegerField()

    def clean_id(self):
        id_value = self.cleaned_data['id']

        if id_value < 1:
            raise forms.ValidationError('Invalid id value. The id must be greater than or equal to 1.')

        return id_value 
    
from django import forms


class OrderTimelineForm(forms.ModelForm):
    class Meta:
        model = OrderTimeline
        fields = ['order_id', 'order', 'status', 'created_on', 'user_id']

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status is None or status < 1:
            raise forms.ValidationError('Status must be greater than or equal to 1.')
        return status

    def clean_created_on(self):
        created_on = self.cleaned_data.get('created_on')
        if created_on is None or created_on < 0:
            raise forms.ValidationError('Created_on cannot be negative.')
        return created_on



class OrderOnlinePaymentForm(forms.ModelForm):
    class Meta:
        model = OrderOnlinePayment
        fields = ['order_id', 'payment_data', 'status', 'timeframe', 'payment_service']

    def clean_status(self):
        status = self.cleaned_data.get('status')
        valid_statuses = ['pending', 'success', 'failed']
        if status not in valid_statuses:
            raise forms.ValidationError('Invalid status.')
        return status

    def clean_timeframe(self):
        timeframe = self.cleaned_data.get('timeframe')
        valid_timeframes = ['instant', 'scheduled']
        if timeframe not in valid_timeframes:
            raise forms.ValidationError('Invalid timeframe.')
        return timeframe
    


class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ['order_id', 'item_id', 'quantity', 'price', 'item_variant_name', 'addon_variants', 'addons_total', 'total', 'brand_id']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity < 1:
            raise forms.ValidationError('Quantity must be greater than or equal to 1.')
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        return price

    def clean_addons_total(self):
        addons_total = self.cleaned_data.get('addons_total')
        if addons_total is None or addons_total < 0:
            raise forms.ValidationError('Addons total cannot be negative.')
        return addons_total

class OrdersEditedForm(forms.ModelForm):
    class Meta:
        model = OrdersEdited
        fields = ['order_id', 'orders', 'items', 'created_on', 'user_id', 'type']

    def clean_orders(self):
        orders = self.cleaned_data.get('orders')
        if not orders or not isinstance(orders, list):
            raise forms.ValidationError('Orders must be a non-empty list.')

        for order in orders:
            if not isinstance(order, dict) or 'order_id' not in order or 'customer_name' not in order:
                raise forms.ValidationError('Each order in orders must be a dictionary with order_id and customer_name fields.')
        return orders

    def clean_items(self):
        items = self.cleaned_data.get('items')
        if not items or not isinstance(items, list):
            raise forms.ValidationError('Items must be a non-empty list.')

        for item in items:
            if not isinstance(item, dict) or 'item_id' not in item or 'quantity' not in item:
                raise forms.ValidationError('Each item in items must be a dictionary with item_id and quantity fields.')
        return items
    
from django.core.exceptions import ValidationError

def get_validator(body):
    if 'order_id' in body:
        if not isinstance(body['order_id'], int):
            raise ValidationError("'order_id' must be an integer.")

    if 'order' in body:
        if body['order'] not in ['asc', 'desc', '']:
            raise ValidationError("'order' must be one of 'asc', 'desc', or an empty string.")

    if 'count' in body:
        if not isinstance(body['count'], int):
            raise ValidationError("'count' must be an integer.")

    if 'offset' in body:
        if not isinstance(body['offset'], int):
            raise ValidationError("'offset' must be an integer.")

    if 'brand_id' in body:
        if not isinstance(body['brand_id'], int):
            raise ValidationError("'brand_id' must be an integer.")

def post_validation(body):
    schema = {
        'order_id': {'type': 'integer', 'required': True},
        'photos': {
            'type': 'list',
            'required': False,
            'schema': {'type': 'string', 'minlength': 4}
        },
        'reviews': {
            'type': 'list',
            'required': True,
            'minlength': 1,
            'schema': {
                'type': 'object',
                'schema': {
                    'type': {'type': 'string', 'valid': list(constants.REVIEW_TYPES.keys()), 'required': True},
                    'type_id': {'type': 'integer', 'required': True},
                    'stars': {'type': 'number', 'min': 1, 'max': 5, 'required': True},
                    'review': {'type': 'string', 'minlength': 3, 'required': True}
                }
            },
            'unique': 'type'
        }
    }

    for key, field in schema.items():
        if key not in body and field.get('required', False):
            raise ValidationError(f"'{key}' is required.")

        if key in body:
            field_type = field.get('type', None)
            if field_type == 'integer':
                if not isinstance(body[key], int):
                    raise ValidationError(f"'{key}' must be an integer.")
            elif field_type == 'list':
                if not isinstance(body[key], list):
                    raise ValidationError(f"'{key}' must be a list.")
                for item in body[key]:
                    if not isinstance(item, field['schema']['type']):
                        raise ValidationError(f"Each item in '{key}' must be of type '{field['schema']['type']}'.")

                    if 'minlength' in field['schema']:
                        if len(item) < field['schema']['minlength']:
                            raise ValidationError(f"Each item in '{key}' must have a length of at least {field['schema']['minlength']}.")

    reviews = body.get('reviews', [])
    if len(reviews) > 0:
        delivery_review_count = sum(1 for review in reviews if review['type'] == constants.REVIEW_TYPES.DELIVERY)
        if delivery_review_count > 1:
            raise ValidationError("Only one delivery review is allowed.")

