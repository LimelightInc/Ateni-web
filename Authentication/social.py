from google.oauth2 import id_token
from google.auth.transport import requests

from backend.models import Client

def auth_by_google(token, client_list):
    try:
    # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request())
        if idinfo['aud'] not in client_list:
            raise ValueError('Could not verify audience.')

        if idinfo['iss'] != 'https://accounts.google.com':
            raise ValueError('Wrong ISS.')

        return idinfo
    except Exception as e:
        raise e




