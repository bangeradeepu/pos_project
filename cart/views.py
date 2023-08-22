from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .validations import ItemValidationForm, PutValidationForm, DeleteValidationForm
from .models import Cart

@csrf_exempt
def post_validation_view(request):
    if request.method == 'POST':
        form = ItemValidationForm(request.POST)
        if form.is_valid():
            # Process the valid form data and save it to the database
            Cart.objects.create(
                customer_id=form.cleaned_data['customer_id'],
                item_id=form.cleaned_data['item_id'],
                quantity=form.cleaned_data['quantity'],
                variant_id=form.cleaned_data['variant_id'],
                addon_variants=form.cleaned_data['addon_variants'],
                created_on=form.cleaned_data['created_on'],
                modified_on=form.cleaned_data['modified_on']
            )
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})

@csrf_exempt
def put_validation_view(request):
    if request.method == 'PUT':
        form = PutValidationForm(request.PUT)
        if form.is_valid():
            cart_id = form.cleaned_data['id']
            try:
                cart = Cart.objects.get(pk=cart_id)
            except Cart.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Cart not found'})

            # Update the cart instance with valid form data
            cart.customer_id = form.cleaned_data['customer_id']
            cart.item_id = form.cleaned_data['item_id']
            cart.quantity = form.cleaned_data['quantity']
            cart.variant_id = form.cleaned_data['variant_id']
            cart.addon_variants = form.cleaned_data['addon_variants']
            cart.modified_on = form.cleaned_data['modified_on']
            cart.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only PUT requests allowed'})

@csrf_exempt
def delete_validation_view(request):
    if request.method == 'DELETE':
        form = DeleteValidationForm(request.DELETE)
        if form.is_valid():
            cart_id = form.cleaned_data['id']
            try:
                cart = Cart.objects.get(pk=cart_id)
                cart.delete()
                return JsonResponse({'status': 'success'})
            except Cart.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Cart not found'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only DELETE requests allowed'})
