from rest_framework import serializers
from .models import AddonCategories, AddonVariants 

class AddonCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddonCategories
        fields = '__all__'


class AddonVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddonVariants
        fields = '__all__'


