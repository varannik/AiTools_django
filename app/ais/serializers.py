from rest_framework import serializers
from .models import SubmitedTool




class SubmitedAiSerializer(serializers.ModelSerializer):
    
    # toolName = ToolNameField()
    # toolUrl =URLField()
    # shortDescription =ShortDescriptionField()
    # review =ReviewField()
    # platform =PlatformField()
    # lunchDate =LunchDateField()
    # logoUrl =LogoUrlField()
    # priceModel =PriceModelField()
    # selectedTag =TagsField()


    class Meta:
        model = SubmitedTool
        fields = [
                'submissionId',
                'respondentId',
                'createdAt',
                'toolName',
                'toolUrl',
                'shortDescription',
                'review',
                'platform',
                'lunchDate',
                'logoUrl',
                'priceModel',
                'selectedTag',
                  ]


class TallySerializer (serializers.Serializer):
    
    submissionId = serializers.CharField(max_length=100)
    respondentId = serializers.CharField(max_length=100)
    createdAt = serializers.DateTimeField()
    fields = serializers.ListField()
