from django.http import HttpResponse

def index(request):
    # You can customize the content of the response
    return HttpResponse("Welcome to KB server!")
