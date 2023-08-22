from rest_framework import serializers
from pos_project.constants import DISPLAY_IN

class RouteValidator:
    @staticmethod
    def get_validator(data):
        class GetValidatorSerializer(serializers.Serializer):
            order = serializers.ChoiceField(choices=['asc', 'desc', ''], allow_blank=True)
            count = serializers.IntegerField()
            offset = serializers.IntegerField()
            brand_id = serializers.IntegerField()

        serializer = GetValidatorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    @staticmethod
    def post_validator(data):
        class PostValidatorSerializer(serializers.Serializer):
            name = serializers.CharField(min_length=3, max_length=100)
            display_in = serializers.ChoiceField(choices=DISPLAY_IN.keys())
            visible = serializers.BooleanField()
            image = serializers.CharField(min_length=3)
            brand_id = serializers.IntegerField()
            mrp_items = serializers.BooleanField()
            single_unavailable = serializers.BooleanField()

        serializer = PostValidatorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    @staticmethod
    def put_validator(data):
        class PutValidatorSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            name = serializers.CharField(min_length=3, max_length=100, required=False)
            visible = serializers.BooleanField(required=False)
            display_in = serializers.ChoiceField(choices=DISPLAY_IN.keys(), required=False)
            image = serializers.CharField(min_length=3, required=False)
            mrp_items = serializers.BooleanField()
            single_unavailable = serializers.BooleanField()

        serializer = PutValidatorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    @staticmethod
    def delete_validator(data):
        class DeleteValidatorSerializer(serializers.Serializer):
            id = serializers.IntegerField()

        serializer = DeleteValidatorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    @staticmethod
    def update_outlet_validator(data):
        class OutletDataSerializer(serializers.Serializer):
            category_id = serializers.IntegerField()
            visible = serializers.BooleanField(required=False)
            rank = serializers.IntegerField(min_value=1, required=False)

        class UpdateOutletValidatorSerializer(serializers.Serializer):
            data = OutletDataSerializer()
            outlets = serializers.ListField(child=serializers.IntegerField())

        serializer = UpdateOutletValidatorSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
