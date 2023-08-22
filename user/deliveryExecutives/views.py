from rest_framework import generics
from django.http import JsonResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from orders.models import Orders
from .models import CheckoutAmountTypes, DECheckout, DECheckoutWithAmount, DeliveryTypes, DeliveryExecutives
from django.shortcuts import render, redirect
from .validations import (
    CheckoutAmountTypesForm, 
    CheckoutPostForm, 
    CheckoutPutForm, 
    CheckoutStatusForm,
    CheckoutSubmitForm,
    CustomForm, 
    PutValidationForm, 
    DeleteValidationForm, 
    OutletBrandValidationForm
)
from pos_project import constants 



def get_de_checkout_details(request, outlet_id, de_id):
    # Fetch the last DECheckout created_on date
    current_checkout_date = DECheckout.objects.filter(
        de_id=de_id
    ).order_by('-created_on').first().created_on

    # Fetch DE Orders from the last DECheckout created_on
    orders = Orders.objects.filter(
        de_id=de_id,
        epoch_time__gt=current_checkout_date,
        payment_mode=constants.PAYMENT_MODE_COD
    )

    # Calculate the total amount of orders
    total = orders.aggregate(models.Sum('total'))['total__sum']

    return JsonResponse({
        'orders': list(orders.values()),
        'total': total if total else 0,
        'current_checkout_date': current_checkout_date
    })



def post_checkout_type(request):
    if request.method == 'POST':
        form = CheckoutAmountTypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = CheckoutAmountTypesForm()

    return render(request, 'your_template.html', {'form': form})

def put_checkout_type(request, checkout_type_id):
    checkout_type = CheckoutAmountTypes.objects.get(pk=checkout_type_id)

    if request.method == 'POST':
        form = CheckoutAmountTypesForm(request.POST, instance=checkout_type)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = CheckoutAmountTypesForm(instance=checkout_type)

    return render(request, 'your_template.html', {'form': form})

def post_checkout(request):
    if request.method == 'POST':
        form = CheckoutPostForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            amounts = form.cleaned_data['amounts']
            # Your processing logic here
            # For example, create a new DECheckoutWithAmount instance for each selected amount
            for amount in amounts:
                DECheckoutWithAmount.objects.create(de_checkout_id=user_id, checkout_amount_id=amount.id, total_count=amount.count)

            return redirect('success_url')  # Redirect to a success page
    else:
        form = CheckoutPostForm()

    return render(request, 'your_template.html', {'form': form})

def put_checkout(request, de_checkout_id):
    de_checkout = DECheckout.objects.get(pk=de_checkout_id)

    if request.method == 'POST':
        form = CheckoutPutForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            amounts = form.cleaned_data['amounts']
            # Your processing logic here
            # For example, update the DECheckoutWithAmount instances for the given de_checkout_id and the selected amounts
            DECheckoutWithAmount.objects.filter(de_checkout_id=de_checkout_id).delete()
            for amount in amounts:
                DECheckoutWithAmount.objects.create(de_checkout_id=de_checkout_id, checkout_amount_id=amount.id, total_count=amount.count)

            return redirect('success_url')  # Redirect to a success page
    else:
        form = CheckoutPutForm(initial={'user_id': de_checkout.user_id, 'amounts': de_checkout.checkoutamounts_set.all()})

    return render(request, 'your_template.html', {'form': form})

def update_checkout_status(request):
    if request.method == 'POST':
        form = CheckoutStatusForm(request.POST)
        if form.is_valid():
            de_checkout_id = form.cleaned_data['de_checkout_id']
            status = form.cleaned_data['status']
            # Your processing logic here
            # For example, update the status of the DECheckout instance
            de_checkout = DECheckout.objects.get(pk=de_checkout_id)
            de_checkout.status = status
            de_checkout.save()

            return redirect('success_url')  # Redirect to a success page
    else:
        form = CheckoutStatusForm()

    return render(request, 'your_template.html', {'form': form})

def submit_checkout(request):
    if request.method == 'POST':
        form = CheckoutSubmitForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['note']
            # Your processing logic here
            # For example, update the note for the DECheckout instance
            de_checkout = DECheckout.objects.get(pk=request.user_id)  # Assuming you have the user_id in the request
            de_checkout.note = note
            de_checkout.save()

            return redirect('success_url')  # Redirect to a success page
    else:
        form = CheckoutSubmitForm()

    return render(request, 'your_template.html', {'form': form})




@csrf_exempt
def delivery_executives_view(request):
    if request.method == 'GET':
        # Handle GET request
        delivery_executives = DeliveryExecutives.objects.all()
        # Convert the queryset to a list of dictionaries
        data = [
            {
                'id': de.id,
                'de_id': de.de_id,
                'name': de.name,
                'address': de.address,
                'phone': de.phone,
                'alternate_phone': de.alternate_phone,
                'dob': de.dob,
                'email': de.email,
                'bank_details': de.bank_details,
                'aadhar_no': de.aadhar_no,
                'aadhar_photo': de.aadhar_photo,
                'dl_photo': de.dl_photo,
                'dl_expiry_date': de.dl_expiry_date,
                'emission_expiry_date': de.emission_expiry_date,
                'emission_photo': de.emission_photo,
                'insurance_photo': de.insurance_photo,
                'insurance_expiry_date': de.insurance_expiry_date,
                'vehicle_photo': de.vehicle_photo,
                'de_photo': de.de_photo,
                'rc_photo': de.rc_photo,
                'device_type': de.device_type,
                'esign': de.esign,
                'status': de.status,
                'created_on': de.created_on,
                'modified_on': de.modified_on,
                'approved': de.approved,
            }
            for de in delivery_executives
        ]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        # Handle POST request
        form = CustomForm(request.POST)
        if form.is_valid():
            # Process the valid form data and create a new DeliveryExecutives object
            delivery_executive = DeliveryExecutives(**form.cleaned_data)
            delivery_executive.save()
            return JsonResponse({'message': 'Delivery Executive created successfully!'})
        else:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)

    elif request.method == 'PUT':
        # Handle PUT request
        form = PutValidationForm(request.PUT)  # You may need to customize the request handling for PUT data
        if form.is_valid():
            de_id = form.cleaned_data['de_id']
            delivery_executive = get_object_or_404(DeliveryExecutives, id=de_id)
            # Update the DeliveryExecutives object with the valid form data
            for key, value in form.cleaned_data.items():
                setattr(delivery_executive, key, value)
            delivery_executive.save()
            return JsonResponse({'message': 'Delivery Executive updated successfully!'})
        else:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)

    elif request.method == 'DELETE':
        # Handle DELETE request
        form = DeleteValidationForm(request.DELETE)  # You may need to customize the request handling for DELETE data
        if form.is_valid():
            de_id = form.cleaned_data['de_id']
            delivery_executive = get_object_or_404(DeliveryExecutives, id=de_id)
            delivery_executive.delete()
            return JsonResponse({'message': 'Delivery Executive deleted successfully!'})
        else:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

@csrf_exempt
def delivery_types_view(request):
    if request.method == 'GET':
        # Handle GET request
        delivery_types = DeliveryTypes.objects.all()
        # Convert the queryset to a list of dictionaries
        data = [
            {
                'id': delivery_type.id,
                'delivery_charge': str(delivery_type.delivery_charge),
                'earning_price': str(delivery_type.earning_price),
                'created_on': delivery_type.created_on,
                'deleted': delivery_type.deleted,
            }
            for delivery_type in delivery_types
        ]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        # Handle POST request
        # Assuming you have a form to validate the POST data for DeliveryTypes model, replace `YourForm` with the actual form class.
        form = OutletBrandValidationForm(request.POST)
        if form.is_valid():
            # Process the valid form data and create a new DeliveryTypes object
            delivery_type = DeliveryTypes(**form.cleaned_data)
            delivery_type.save()
            return JsonResponse({'message': 'Delivery Type created successfully!'})
        else:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)

    # Other HTTP methods can be handled similarly.
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

