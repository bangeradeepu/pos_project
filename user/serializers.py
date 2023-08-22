from rest_framework import serializers
from .models import Users, UserCompanyLink

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserCompanyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompanyLink
        fields = '__all__'
