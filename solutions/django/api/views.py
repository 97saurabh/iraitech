from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .serializers import Serializer
def sum(n,x):
    total = 0
    
    
    for i in range(1, n+1):
        total = total + (1 / x)**i
    return total



@api_view(['POST',])
def solution(request):
    if request.method == 'POST':

        serializer = Serializer(data=request.data)
        data = {}
        if serializer.is_valid():

            x = serializer.data['x']
            n = serializer.data['a']

            data['result'] = sum(n,x)

        else:
            data = serializer.errors
        return Response(data)
