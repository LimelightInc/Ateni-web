from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings    
from django.utils.decorators import method_decorator
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import jwt

from backend.Api.v1.serializers import UserLoginSerializer, UserSignupSerializer
from backend.models import User
from Authentication import authenticate_user_by_email_and_password, signup_with_email_and_password
from Decorators import allowed_client


#TODO: Make custom decorator to check login and client_id
class LoginView(APIView):

    @method_decorator(allowed_client())
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
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
        return Response({'status': 'Failed', 'message':'Not provided all required info.'}, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):

    @method_decorator(allowed_client())
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if request.data.get('email') and request.data.get('password') and request.data.get('username'):
            if serializer.is_valid():    
                email = request.data.get('email') 
                password = request.data.get('password')
                username = request.data.get('username')
                auth_user= signup_with_email_and_password(username, email, password)
                if auth_user['status'] == 'Success':
                    return Response(auth_user, status=status.HTTP_201_CREATED)
                return Response(auth_user, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status': 'Failed', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Failed', 'message':'Not provided all required info.'}, status=status.HTTP_400_BAD_REQUEST)
