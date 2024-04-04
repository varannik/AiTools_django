from rest_framework import serializers
from .models import SubmitedTool


class SubmitedAiSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = SubmitedTool
        fields = "__all__"
                
        extra_kwargs = {
        'shortDescription': {'required': False},
        'review': {'required': False},
        'platform': {'required': False},
        'lunchDate': {'required': False},
        'logoUrl': {'required': False},
        'priceModel': {'required': False},  
                        }