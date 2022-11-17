from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Carserializer
from . models import Car

@api_view(['GET','POST'])
def cars_list(request):
    
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = Carserializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Carserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
