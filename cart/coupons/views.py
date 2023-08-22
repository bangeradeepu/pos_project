from .models import CouponCodes, CustomerCuponUsage, InfluencerCouponCodes, CouponOutletLink
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .validations import (
    CouponPostSerializer,
    CouponPutSerializer,
    CouponDeleteSerializer,
    CouponGetSerializer,
    CustomerCouponSerializer,
    InfluencerCouponSerializer,
    CouponOutletLinkValidatior,

)



@api_view(['POST'])
def create_coupon(request):
    serializer = CouponPostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_coupon(request):
    try:
        coupon_id = request.data.get('id')
        coupon = CouponCodes.objects.get(pk=coupon_id)
    except CouponCodes.DoesNotExist:
        return Response({"error": "Coupon not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CouponPutSerializer(coupon, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_coupon(request):
    serializer = CouponDeleteSerializer(data=request.data)

    if serializer.is_valid():
        coupon_id = serializer.validated_data['id']
        try:
            coupon = CouponCodes.objects.get(pk=coupon_id)
            coupon.delete()
            return Response({"message": "Coupon deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except CouponCodes.DoesNotExist:
            return Response({"error": "Coupon not found"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_coupons(request):
    serializer = CouponGetSerializer(data=request.query_params)

    if serializer.is_valid():
        coupons = CouponCodes.objects.all()

        coupon_id = serializer.validated_data.get('id')
        if coupon_id is not None:
            coupons = coupons.filter(id=coupon_id)

        code = serializer.validated_data.get('code')
        if code:
            coupons = coupons.filter(code=code)

        brand_id = serializer.validated_data.get('brand_id')
        if brand_id is not None:
            coupons = coupons.filter(brand_id=brand_id)

        order = serializer.validated_data.get('order')
        if order == 'asc':
            coupons = coupons.order_by('id')
        elif order == 'desc':
            coupons = coupons.order_by('-id')

        count = serializer.validated_data.get('count')
        offset = serializer.validated_data.get('offset')
        if count is not None and offset is not None:
            coupons = coupons[offset:offset + count]

        return Response({'coupons': coupons}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_customer_coupon(request):
    serializer = CustomerCouponSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_customer_coupon(request):
    try:
        customer_coupon_id = request.data.get('id')
        customer_coupon = CustomerCuponUsage.objects.get(pk=customer_coupon_id)
    except CustomerCuponUsage.DoesNotExist:
        return Response({"error": "Customer coupon not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CustomerCouponSerializer(customer_coupon, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer_coupon(request):
    try:
        customer_coupon_id = request.data.get('id')
        customer_coupon = CustomerCuponUsage.objects.get(pk=customer_coupon_id)
    except CustomerCuponUsage.DoesNotExist:
        return Response({"error": "Customer coupon not found"}, status=status.HTTP_404_NOT_FOUND)

    customer_coupon.delete()
    return Response({"message": "Customer coupon deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_customer_coupons(request):
    serializer = CustomerCouponSerializer(data=request.query_params, many=True)

    if serializer.is_valid():
        customer_coupons = CustomerCuponUsage.objects.all()

        coupon_id = serializer.validated_data.get('coupon_id')
        if coupon_id:
            customer_coupons = customer_coupons.filter(coupon__id=coupon_id)

        customer_phone = serializer.validated_data.get('customer_phone')
        if customer_phone:
            customer_coupons = customer_coupons.filter(customer_phone=customer_phone)

        order = serializer.validated_data.get('order')
        if order == 'asc':
            customer_coupons = customer_coupons.order_by('id')
        elif order == 'desc':
            customer_coupons = customer_coupons.order_by('-id')

        count = serializer.validated_data.get('count')
        offset = serializer.validated_data.get('offset')
        if count is not None and offset is not None:
            customer_coupons = customer_coupons[offset:offset + count]

        return Response(CustomerCouponSerializer(customer_coupons, many=True).data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_influencer_coupon(request):
    serializer = InfluencerCouponSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_influencer_coupon(request):
    try:
        influencer_coupon_id = request.data.get('id')
        influencer_coupon = InfluencerCouponCodes.objects.get(pk=influencer_coupon_id)
    except InfluencerCouponCodes.DoesNotExist:
        return Response({"error": "Influencer coupon not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = InfluencerCouponSerializer(influencer_coupon, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_influencer_coupon(request):
    try:
        influencer_coupon_id = request.data.get('id')
        influencer_coupon = InfluencerCouponCodes.objects.get(pk=influencer_coupon_id)
    except InfluencerCouponCodes.DoesNotExist:
        return Response({"error": "Influencer coupon not found"}, status=status.HTTP_404_NOT_FOUND)

    influencer_coupon.delete()
    return Response({"message": "Influencer coupon deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_influencer_coupons(request):
    serializer = InfluencerCouponSerializer(data=request.query_params, many=True)

    if serializer.is_valid():
        influencer_coupons = InfluencerCouponCodes.objects.all()

        coupon_id = serializer.validated_data.get('coupon_id')
        if coupon_id:
            influencer_coupons = influencer_coupons.filter(coupon__id=coupon_id)

        phone = serializer.validated_data.get('phone')
        if phone:
            influencer_coupons = influencer_coupons.filter(phone=phone)

        order = serializer.validated_data.get('order')
        if order == 'asc':
            influencer_coupons = influencer_coupons.order_by('id')
        elif order == 'desc':
            influencer_coupons = influencer_coupons.order_by('-id')

        count = serializer.validated_data.get('count')
        offset = serializer.validated_data.get('offset')
        if count is not None and offset is not None:
            influencer_coupons = influencer_coupons[offset:offset + count]

        return Response(InfluencerCouponSerializer(influencer_coupons, many=True).data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def create_coupon_outlet_link(request):
    if request.method == 'POST':
        data = request.POST.dict()  # Assuming you're sending data in POST request body
        validator = CouponOutletLinkValidatior.get_validator(data)
        
        if validator:
            return JsonResponse({'status': 'error', 'errors': validator.message_dict})
        
        try:
            coupon_outlet_link = CouponOutletLink(**data)
            coupon_outlet_link.save()
            return JsonResponse({'status': 'success', 'message': 'Coupon outlet link created successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})