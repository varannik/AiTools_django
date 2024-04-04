from rest_framework import serializers
from core.models import CMST


class TagsRelations(serializers.ModelSerializer):
    
    class Meta:
        model = CMST
        fields = "__all__"


class Tags(serializers.Serializer):

    tags = serializers.CharField(max_length=500)


class MS(serializers.Serializer):

    MainSub = serializers.CharField(max_length=20000)


class CA(serializers.Serializer):

    Career = serializers.CharField(max_length=20000)


class AiURL(serializers.Serializer):

    URL = serializers.URLField() 


class LCTReq(serializers.Serializer):
    '''LangChain pipeline requested fields - Serializer to Request tagging for desired URL'''

    URL = serializers.URLField()
    short_description = serializers.BooleanField(default=True)
    review = serializers.BooleanField(default=True)
    pricing = serializers.BooleanField(default=True)
    topic_selection = serializers.BooleanField(default=True)
    platform = serializers.BooleanField(default=True)
    lunch_date = serializers.BooleanField(default=True)


class LCTRes(serializers.Serializer):
    '''LangChain pipeline response - Serializer for returned JSON by LLM'''

    URL = serializers.URLField()
    short_description = serializers.CharField(max_length=None)
    review = serializers.CharField(max_length=None)
    pricing = serializers.ListField(max_length=None)
    topic_selection = serializers.ListField(max_length=None)
    platform = serializers.ListField(max_length=None)
    lunch_date = serializers.DateField()