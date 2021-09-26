from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.

@api_view(['GET', 'POST'])
def Data_list(request):
  
    if request.method == 'GET':
        Data = Task_model.objects.all()
        serializer = Task_modelSerializer(Data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Task_modelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE' ])
def Data_detail(request, pk):

    try:
        Data = Task_model.objects.get(pk=pk)
    except Task_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Task_modelSerializer(Data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Task_modelSerializer(Data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class SnippetViewSet(viewsets.ModelViewSet):
    
#     queryset = Task_model.objects.all()
#     serializer_class = Task_modelSerializer