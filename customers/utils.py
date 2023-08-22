from .models import CustomerAddresses

def doesAddressExist(address_id, customer_id):
    try:
        addressDetails = CustomerAddresses.objects.get(
            id=address_id, customer_id=customer_id, deleted=False
        )
        return True
    except CustomerAddresses.DoesNotExist:
        return False
