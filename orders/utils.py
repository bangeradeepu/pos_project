from .generalSettings.models import GeneralSettings
from pos_project import constants

def total(database, coupon_data, items_total, items_total_for_discount, delivery_type, outlet):
    additional_charges = 0
    discount = 0
    total = 0

    # Check coupon code
    if coupon_data:
        if coupon_data.coupon_type == constants.COUPON_TYPE.PERCENTAGE and items_total > coupon_data.minimum_total:
            discount = (items_total_for_discount * coupon_data.percentage_off) / 100
            discount = min(discount, coupon_data.cap)
        elif items_total_for_discount > coupon_data.minimum_total:
            discount = coupon_data.amount_off

    # Calculate total of all additional charges
    try:
        additional_charges_data = GeneralSettings.objects.get(attribute=constants.GENERAL_SETTINGS.ADDITIONAL_CHARGES)
        for additional_charge in additional_charges_data.value:
            additional_charges += additional_charge.get('charge', 0)
    except GeneralSettings.DoesNotExist:
        pass

    # Calculate total price
    total = items_total - discount + additional_charges
    return {
        'total': total,
        'additionalChargesData': additional_charges_data,
    }
