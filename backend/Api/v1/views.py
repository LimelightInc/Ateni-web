from django.http import request
from django.http import cookie
from django.http.response import Http404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings    
from django.utils.decorators import method_decorator
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import jwt

from backend.Api.v1.serializers import *
from backend.models import *
from Authentication import authenticate_user_by_email_and_password, signup_with_email_and_password
from Decorators import allowed_client, is_logged_in

from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets



#Auth apis
#TODO: Make custom decorator to check login and client_id
class LoginView(APIView):
    @method_decorator(is_logged_in())
    def get(self, request):
        users = User.objects.all()
        serializer = UserLoginSerializer(users, many=True)
        return Response(serializer.data)

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



#Model apis #todo: MOWIKI
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    ''' viewset to automatically 'list' and 'detail' actions '''
    queryset = User.objects.all()
    serializer_class =  UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = Profile.objects.all()
    serializer_class =  UserProfileSerializer
    # permission_classes


class InterestViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = Interest.objects.all()
    serializer_class =  InterestSerializer


class InnerCircleViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = InnerCircle.objects.all()
    serializer_class =  InnerCircleSerializer


class LevelViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = Level.objects.all()
    serializer_class =  LevelSerializer


class CommunityViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = Community.objects.all()
    serializer_class =  CommunityDetailSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = Project.objects.all()
    serializer_class =  ProjectDetailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = Comment.objects.all()
    serializer_class =  CommentDetailSerializer


class SubCommentViewSet(viewsets.ModelViewSet):
    ''' viewset to automatically 'list', 'create', 'retrieve', 'update', and 'destroy' actions '''
    queryset = SubComment.objects.all()
    serializer_class =  SubCommentSerializer