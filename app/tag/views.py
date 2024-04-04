from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from core.models import CMST
from .serializers import Tags , MS, CA, LCTReq , LCTRes
from .modules.extractor import *
from .modules.lcTagging import SORLLM
from .modules.modifier import ReplaceStrToList



class RetrieveMainSub(APIView):
    '''Return Main and Sub categories base on posted tags'''
    
    def post(self, request):
        serializer_in =  Tags(data = request.data)
        serializer_in.is_valid(raise_exception=True)

        tags = TagList(serializer_in.data['tags'])

        
        serializer_out = MS(data = {'MainSub':MainSubStr(tags, model=CMST)})
        serializer_out.is_valid(raise_exception=True)

        return Response(serializer_out.data, status=status.HTTP_200_OK)
    


class RetrieveCareer(APIView):
    '''Return related careers base on posted tags'''
    
    def post(self, request):
        serializer_in =  Tags(data = request.data)
        serializer_in.is_valid(raise_exception=True)

        tags = TagList(serializer_in.data['tags'])

        
        serializer_out = CA(data = {'Career':CareerStr(tags, model=CMST)})
        serializer_out.is_valid(raise_exception=True)

        return Response(serializer_out.data, status=status.HTTP_200_OK)


class Tagging(APIView):
    '''Tag all properties of a posted URL'''
    
    def post(self, request):
        serializer_in= LCTReq(data=request.data)
        serializer_in.is_valid(raise_exception=True)

        llmResult = SORLLM(serializer_in.data)
        print(llmResult)
        modifiedData = ReplaceStrToList(llmResult)
        print(modifiedData)

        serializer_out = LCTRes(data = modifiedData)
        serializer_out.is_valid(raise_exception=True)

        return Response(serializer_out.data, status=status.HTTP_200_OK)