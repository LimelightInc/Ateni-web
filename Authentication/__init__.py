from django.contrib.auth.hashers import check_password
from django.conf import settings
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

import jwt

from Authentication import social 
from backend.models import Client
from backend.models import User

def authenticate_user_by_email_and_password(email, password):
    #Check if user exists
    if not check_if_user_exists(email):
        return {'status': 'Failed', 'message': 'User with that email does not exist.'}
    
    #Check if the user email and password match
    user_detail = verify_user(email, password)
    if not user_detail:
        return {'status': 'Failed', 'message': 'Email or Password Incorrect'}
    
    #Generate auth token for the user
    user_id = user_detail.id
    print('User id is ')
    print(user_id)
    return {'status': 'Success', 'token': generate_auth_token(user_id)}

def authenticate_user_by_google(google_client_token):
    #Get all the valid client applications
    client_list = get_all_clients()

    #Decode client_user token and check validity.
    auth_data = social.auth_by_google(google_client_token, client_list)
    if auth_data:
        email = auth_data['email']
        if not check_if_user_exists(email):
            #TODO: Signup User if they do not exist while google sign in.
            pass

        user_id = get_user_detail(email).id
        return generate_auth_token(user_id)

    return {'status': 'Failed', 'message': 'Authentication Failed. Please try again later.'}

def generate_auth_token(user_id):
    PRIVATE_KEY = getattr(settings, "PRIVATE_KEY")
    
    PRIVATE_KEY = serialization.load_pem_private_key(PRIVATE_KEY.encode(), password=None, backend=default_backend())
    print(PRIVATE_KEY)
    return jwt.encode({'user_id': user_id}, PRIVATE_KEY, algorithm='RS256' ).decode('utf-8')
    
def check_if_user_exists(email):
    if not User.objects.filter(email = email).exists():
        return False
    return True

def get_all_clients():
    client_list = []
    for client in Client.objects.all():
        client_list.append(client.identifier)


def verify_user(email, password):
    user = User.objects.filter(email=email).first()
    
    if not user.check_password(password):
        return False
    return user