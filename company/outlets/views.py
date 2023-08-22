from django.http import JsonResponse
from .validations import GetValidatorForm, PostValidatorForm, PutValidatorForm
from .models import Outlets, CompanyOutlets

# View for handling GET request with GetValidatorForm for Outlets model
def get_outlets(request):
    if request.method == 'GET':
        form = GetValidatorForm(request.GET)
        if form.is_valid():
            # Process valid form data here
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            company_id = form.cleaned_data['company_id']
            order = form.cleaned_data['order']
            count = form.cleaned_data['count']
            offset = form.cleaned_data['offset']
            
            # Perform some actions with the data or fetch data from the models
            # and return a JSON response
            # Example:
            outlets_data = Outlets.objects.filter(company_id=company_id, created_on__range=(start_date, end_date)).order_by(order)
            data = [{"id": outlet.id, "name": outlet.name} for outlet in outlets_data]
            return JsonResponse({'data': data})
        else:
            # Handle invalid form data here
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = GetValidatorForm()
    return JsonResponse({'errors': 'Invalid request method'}, status=405)


# View for handling POST request with PostValidatorForm for Outlets model
def create_outlet(request):
    if request.method == 'POST':
        form = PostValidatorForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            outlet = form.save()
            return JsonResponse({'message': 'Outlet created successfully', 'data': {'id': outlet.id}})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = PostValidatorForm()
    return JsonResponse({'errors': 'Invalid request method'}, status=405)


# View for handling PUT request with PutValidatorForm for Outlets model
def update_outlet(request):
    if request.method == 'PUT':
        form = PutValidatorForm(request.PUT, instance=Outlets())
        if form.is_valid():
            # Save the valid form data to the database
            outlet = form.save()
            return JsonResponse({'message': 'Outlet updated successfully', 'data': {'id': outlet.id}})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = PutValidatorForm()
    return JsonResponse({'errors': 'Invalid request method'}, status=405)


# View for handling GET request with GetValidatorForm for CompanyOutlets model
def get_company_outlets(request):
    if request.method == 'GET':
        form = GetValidatorForm(request.GET)
        if form.is_valid():
            # Process valid form data here
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            company_id = form.cleaned_data['company_id']
            order = form.cleaned_data['order']
            count = form.cleaned_data['count']
            offset = form.cleaned_data['offset']
            
            # Perform some actions with the data or fetch data from the models
            # and return a JSON response
            # Example:
            company_outlets_data = CompanyOutlets.objects.filter(company_id=company_id, created_on__range=(start_date, end_date)).order_by(order)
            data = [{"id": outlet.id, "name": outlet.name} for outlet in company_outlets_data]
            return JsonResponse({'data': data})
        else:
            # Handle invalid form data here
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = GetValidatorForm()
    return JsonResponse({'errors': 'Invalid request method'}, status=405)


# View for handling POST request with PostValidatorForm for CompanyOutlets model
def create_company_outlet(request):
    if request.method == 'POST':
        form = PostValidatorForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            company_outlet = form.save()
            return JsonResponse({'message': 'Company outlet created successfully', 'data': {'id': company_outlet.id}})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = PostValidatorForm()
    return JsonResponse({'errors': 'Invalid request method'}, status=405)


# View for handling PUT request with PutValidatorForm for CompanyOutlets model
def update_company_outlet(request):
    if request.method == 'PUT':
        form = PutValidatorForm(request.PUT, instance=CompanyOutlets())
        if form.is_valid():
            # Save the valid form data to the database
            company_outlet = form.save()
            return JsonResponse({'message': 'Company outlet updated successfully', 'data': {'id': company_outlet.id}})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = PutValidatorForm()
    return JsonResponse({'errors': 'Invalid request method'}, status=405)
