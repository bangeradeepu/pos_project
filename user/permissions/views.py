from django.http import JsonResponse
from .models import Permissions, Modules, Roles, UserRoles
from .validations import AddPermissionsForm, DeletePermissionsForm, AddRoleForm, AddRoleToUserForm

# View to list all permissions
def list_permissions_view(request):
    permissions = Permissions.objects.all()
    data = [{'role_id': p.role_id, 'module_id': p.module_id, 'create': p.create, 'read': p.read, 'update': p.update, 'delete': p.delete} for p in permissions]
    return JsonResponse(data, safe=False)

# View to add permissions
def add_permissions_view(request):
    if request.method == 'POST':
        form = AddPermissionsForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            role_id = form.cleaned_data['role_id']
            module_id = form.cleaned_data['module_id']
            create = form.cleaned_data['create']
            read = form.cleaned_data['read']
            update = form.cleaned_data['update']
            delete = form.cleaned_data['delete']
            permission = Permissions(role_id=role_id, module_id=module_id, create=create, read=read, update=update, delete=delete)
            permission.save()
            return JsonResponse({'message': 'Permissions added successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Only POST method is allowed'}, status=405)

# View to delete permissions
def delete_permissions_view(request):
    if request.method == 'POST':
        form = DeletePermissionsForm(request.POST)
        if form.is_valid():
            # Delete the permissions from the database
            role_id = form.cleaned_data['role_id']
            module_id = form.cleaned_data.get('module_id')
            permissions = Permissions.objects.filter(role_id=role_id)
            if module_id:
                permissions = permissions.filter(module_id=module_id)
            permissions.delete()
            return JsonResponse({'message': 'Permissions deleted successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Only POST method is allowed'}, status=405)

# View to list all roles
def list_roles_view(request):
    roles = Roles.objects.all()
    data = [{'id': r.id, 'name': r.name, 'created_by': r.created_by, 'created_on': r.created_on} for r in roles]
    return JsonResponse(data, safe=False)

# View to add a role
def add_role_view(request):
    if request.method == 'POST':
        form = AddRoleForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            name = form.cleaned_data['name']
            created_by = 1  # You can set the created_by field based on the current user
            role = Roles(name=name, created_by=created_by)
            role.save()
            return JsonResponse({'message': 'Role added successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Only POST method is allowed'}, status=405)

# View to list all user roles
def list_user_roles_view(request):
    user_roles = UserRoles.objects.all()
    data = [{'user_id': ur.user_id, 'role_id': ur.role_id, 'company_id': ur.company_id, 'outlet_id': ur.outlet_id} for ur in user_roles]
    return JsonResponse(data, safe=False)

# View to add a role to a user
def add_role_to_user_view(request):
    if request.method == 'POST':
        form = AddRoleToUserForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            role_id = form.cleaned_data['role_id']
            user_id = form.cleaned_data['user_id']
            outlet_id = form.cleaned_data['outlet_id']
            company_id = 1  # You can set the company_id based on the current user's company
            user_role = UserRoles(user_id=user_id, role_id=role_id, company_id=company_id, outlet_id=outlet_id)
            user_role.save()
            return JsonResponse({'message': 'Role added to user successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Only POST method is allowed'}, status=405)

# View to list all modules
def list_modules_view(request):
    modules = Modules.objects.all()
    data = [{'id': m.id, 'name': m.name} for m in modules]
    return JsonResponse(data, safe=False)
