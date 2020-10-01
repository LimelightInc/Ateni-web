from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import jwt

from backend.Api.v1.serializers import UserSerializer
from backend.models import User
from Authentication import authenticate_user_by_email_and_password

class LoginView(APIView):
    # def get(self, request):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if request.data.get('email') and request.data.get('password'):
            if serializer.is_valid():    
                email = request.data.get('email') 
                password = request.data.get('password')
                auth_user= authenticate_user_by_email_and_password(email, password)
                if auth_user['status'] == 'Success':
                    return Response(auth_user, status=status.HTTP_201_CREATED)
                return Response(auth_user, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status': 'Failed', 'message': 'Wrong data format passed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)