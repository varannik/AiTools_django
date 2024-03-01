from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from .models import SubmitedTool
from .serializers import SubmitedAiSerializer , TallySerializer
import json



def searchInDict(data, title):
    for i in data['fields']:
        if i['label'] == title:
            return i['value']

def searchInDictUrl(data, title):
    for i in data['fields']:
        if i['label'] == title:
            if 'http' in i['value']:
                return i['value']
            else: 
                return 'https://' + i['value']
        

def searchInDictOption(data, title):

    for i in data['fields']:
        if i['label'] == title:
            valList = i['value']
            options = i['options']
            res = []
            for v in valList:
                for o in options:
                    if o['id']==v:
                        res.append(o['text'])
            resStr = str(res).replace("[", "").replace("]","").replace("'", "")
            return resStr

def searchInDictLogo(data, title):

    urls =[]
    for i in data['fields']:

        if i['label'] == title:
            uv = i['value']

            for u in uv: 
                urls.append(u['url'])
    UrlsStr = str(urls).replace("[", "").replace("]","").replace("'", "")                
    return UrlsStr




def reformatResponse(data):
    '''Reformat response data from tally API'''

    d = dict()
    d.update({
    
        'submissionId': data['submissionId'],
        'respondentId':data['respondentId'],
        'createdAt':data['createdAt'],
        'toolName':searchInDict(data, 'Tool Name'),
        'toolUrl':searchInDictUrl(data, 'URL'),
        'shortDescription':searchInDict(data, 'Short Description'),
        'review':searchInDict(data, 'Review'),
        'platform':searchInDictOption(data, 'Platform'),
        'lunchDate':searchInDict(data, 'Enter Date of tool launch'),
        'logoUrl':searchInDictLogo(data, 'Logo'),
        'priceModel':searchInDictOption(data, 'Pricing Models'),
        'selectedTag':searchInDictOption(data, 'Choose at least 2 Topics from  the list below:'),

    })
    return d

class SubmitedToolView(APIView):
      
    def get(self, request):
        tool = get_object_or_404(SubmitedTool)
        ser = SubmitedAiSerializer(tool)
        return Response(ser.data)
    
    def post(self, request):

        serializer = SubmitedAiSerializer(data=reformatResponse(request.data['data']))
        
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        




