from rest_framework import generics
from .models import Users, UserCompanyLink
from .serializers import UsersSerializer, UserCompanyLinkSerializer

class UsersListView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserCompanyLinkListView(generics.ListCreateAPIView):
    queryset = UserCompanyLink.objects.all()
    serializer_class = UserCompanyLinkSerializer

class UserCompanyLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCompanyLink.objects.all()
    serializer_class = UserCompanyLinkSerializer
