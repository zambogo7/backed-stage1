from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
import rest_framework

from stage1.models import Stage1
from stage1.serializers import Stage1Serializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def details(request):
    if request.method == 'GET':
        userDetails = Stage1.objects.all()
        
        slackUsername = request.query_params.get('slackUsername', None)
        if slackUsername is not None:
            userDetails = userDetails.filter(title__icontains=slackUsername)
        
        userDetails_serializer = Stage1Serializer(userDetails, many=True)
        return JsonResponse(userDetails_serializer.data, safe=False)
    
    elif request.method == 'POST':
        stage1_data = JSONParser().parse(request)
        stage1_serializer = Stage1Serializer(data=stage1_data)
        if stage1_serializer.is_valid():
            stage1_serializer.save()
            return JsonResponse(stage1_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(stage1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Stage1.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.

