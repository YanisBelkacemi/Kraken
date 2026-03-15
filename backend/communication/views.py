from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import utils
from rest_framework.permissions import IsAuthenticated
from .serializer import APIkeyserializer
from User.models import Users
# Create your views here.

class ApiKeyCreation(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self , request):
        APIkey = APIkeyserializer(data = request.data , context = {"request" : request})
        if APIkey.is_valid():
            APItoken = APIkey.save()
            return Response({
                'user' : APItoken.name,
                "key" : APItoken.key_hash,
                #'owner' : Users.objects.get(id = APItoken.user_id.username).username

            })
        return Response({"error" : APIkey.error_messages, 'name' : APIkey.data})