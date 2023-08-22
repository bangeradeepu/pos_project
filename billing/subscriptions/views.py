from rest_framework import generics
from .models import Subscription, ActiveSubscriptions, PaymentDetails
from .serializers import SubscriptionSerializer, ActiveSubscriptionsSerializer, PaymentDetailsSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

# Views for Subscription model
class SubscriptionListView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

# Views for ActiveSubscriptions model
class ActiveSubscriptionsListView(generics.ListCreateAPIView):
    queryset = ActiveSubscriptions.objects.all()
    serializer_class = ActiveSubscriptionsSerializer

class ActiveSubscriptionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActiveSubscriptions.objects.all()
    serializer_class = ActiveSubscriptionsSerializer

# Views for PaymentDetails model
class PaymentDetailsListView(generics.ListCreateAPIView):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer

class PaymentDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer


@require_POST
def create_subscription(request):
    data = json.loads(request.body)
    
    name = data.get('name')
    price = data.get('price')
    duration = data.get('duration')
    features = data.get('features')
    
    if name and price is not None and duration is not None and features is not None:
        # Create a new subscription manually
        subscription = Subscription.objects.create(name=name, price=price, duration=duration, features=features)
        return JsonResponse({'message': 'Subscription created successfully', 'data': {'id': subscription.id}})
    else:
        return JsonResponse({'error': 'Invalid data provided'}, status=400)