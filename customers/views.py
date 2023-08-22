# views.py
from rest_framework import generics
from .models import Customers, CustomerAddresses
from .serializers import CustomersSerializer, CustomerAddressesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .validations import (
    AddressGetValidation,
    PostCustomerAddressValidation, 
    PutCustomerAddressValidation, 
    DeleteCustomerAddressValidation,
    PostValidation, 
    PutValidation, 
    DeleteValidator,
)


class AddressView(APIView):
    def get(self, request):
        # Validate the request data
        serializer = AddressGetValidation(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the GET request with validated data
        customer_id = serializer.validated_data.get("customer_id")
        count = serializer.validated_data.get("count")
        offset = serializer.validated_data.get("offset")

        try:
            # Your logic to fetch addresses based on customer_id and apply pagination here
            addresses = CustomerAddresses.objects.filter(customer_id=customer_id)
            total_count = addresses.count()

            # Applying pagination
            addresses = addresses[offset: offset + count]

            # Serialize the data and return the response
            serialized_data = CustomerAddressesSerializer(addresses, many=True).data

            return Response(
                {
                    "data": serialized_data,
                    "total_count": total_count,
                    "count": count,
                    "offset": offset,
                }
            )

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        # Validate the request data
        serializer = PostCustomerAddressValidation(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the POST request with validated data
        customer_id = serializer.validated_data.get("customer_id")
        address = serializer.validated_data.get("address")
        locality = serializer.validated_data.get("locality")
        coordinates = serializer.validated_data.get("coordinates")
        address_type = serializer.validated_data.get("type")
        other_tag = serializer.validated_data.get("other_tag")

        # Your logic to process the POST request here
        # For example, create a new CustomerAddresses instance and save it to the database
        try:
            new_address = CustomerAddresses(
                customer_id=customer_id,
                address=address,
                locality=locality,
                coordinates=coordinates,
                type=address_type,
                other_tag=other_tag,
            )
            new_address.save()

            # Serialize the data and return the response
            serialized_data = CustomerAddressesSerializer(new_address).data

            return Response(serialized_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        # Validate the request data
        serializer = PutCustomerAddressValidation(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the PUT request with validated data
        customer_id = serializer.validated_data.get("customer_id")
        address_id = serializer.validated_data.get("id")
        address = serializer.validated_data.get("address")
        locality = serializer.validated_data.get("locality")
        coordinates = serializer.validated_data.get("coordinates")
        address_type = serializer.validated_data.get("type")
        other_tag = serializer.validated_data.get("other_tag")

        try:
            # Your logic to update the CustomerAddresses instance here
            address_instance = CustomerAddresses.objects.get(customer_id=customer_id, id=address_id)

            if address:
                address_instance.address = address
            if locality:
                address_instance.locality = locality
            if coordinates:
                address_instance.coordinates = coordinates
            if address_type:
                address_instance.type = address_type
            if other_tag:
                address_instance.other_tag = other_tag

            address_instance.save()

            # Serialize the data and return the response
            serialized_data = CustomerAddressesSerializer(address_instance).data

            return Response(serialized_data)

        except CustomerAddresses.DoesNotExist:
            return Response("Address not found.", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        # Validate the request data
        serializer = DeleteCustomerAddressValidation(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the DELETE request with validated data
        customer_id = serializer.validated_data.get("customer_id")
        address_id = serializer.validated_data.get("id")

        try:
            # Your logic to delete the CustomerAddresses instance here
            address_instance = CustomerAddresses.objects.get(customer_id=customer_id, id=address_id)
            address_instance.delete()

            return Response("Address deleted successfully.")

        except CustomerAddresses.DoesNotExist:
            return Response("Address not found.", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CustomersView(APIView):
    def post(self, request):
        # Validate the request data
        serializer = PostValidation(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the POST request with validated data
        # Assuming you have a model called Customers, you can create a new instance and save it to the database
        try:
            new_customer = Customers(
                name=serializer.validated_data.get("name"),
                phone=serializer.validated_data.get("phone"),
                alt_phone=serializer.validated_data.get("alt_phone"),
                photo=serializer.validated_data.get("photo"),
                email=serializer.validated_data.get("email"),
            )
            new_customer.save()

            # Serialize the data and return the response
            serialized_data = CustomersSerializer(new_customer).data

            return Response(serialized_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        # Validate the request data
        serializer = PutValidation(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the PUT request with validated data
        customer_id = serializer.validated_data.get("id")

        try:
            # Your logic to update the Customers instance here
            customer_instance = Customers.objects.get(id=customer_id)

            if serializer.validated_data.get("name"):
                customer_instance.name = serializer.validated_data.get("name")
            if serializer.validated_data.get("phone"):
                customer_instance.phone = serializer.validated_data.get("phone")
            if serializer.validated_data.get("alt_phone"):
                customer_instance.alt_phone = serializer.validated_data.get("alt_phone")
            if serializer.validated_data.get("photo"):
                customer_instance.photo = serializer.validated_data.get("photo")
            if serializer.validated_data.get("email"):
                customer_instance.email = serializer.validated_data.get("email")
            if serializer.validated_data.get("login_status"):
                customer_instance.login_status = serializer.validated_data.get("login_status")

            customer_instance.save()

            # Serialize the data and return the response
            serialized_data = CustomersSerializer(customer_instance).data

            return Response(serialized_data)

        except Customers.DoesNotExist:
            return Response("Customer not found.", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        # Validate the request data
        serializer = DeleteValidator(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process the DELETE request with validated data
        customer_id = serializer.validated_data.get("id")

        try:
            # Your logic to delete the Customers instance here
            customer_instance = Customers.objects.get(id=customer_id)
            customer_instance.delete()

            return Response("Customer deleted successfully.")

        except Customers.DoesNotExist:
            return Response("Customer not found.", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

