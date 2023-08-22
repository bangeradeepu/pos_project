from rest_framework import serializers
from .models import Subscription, ActiveSubscriptions, PaymentDetails

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class ActiveSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveSubscriptions
        fields = '__all__'

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'
