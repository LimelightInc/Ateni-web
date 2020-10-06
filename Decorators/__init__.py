from functools import wraps
from rest_framework.response import Response
from rest_framework import status

from Authentication import get_all_clients, verify_user_from_token

def allowed_client():
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            client_id = request.data.get('client_id')
            if client_id in get_all_clients():
                return function(request, *args, **kwargs)
            else:
                return Response({'status':'Failed', 'message': 'Client not authorized.'}, status=status.HTTP_403_FORBIDDEN)
        return wrapper
    return decorator


def is_logged_in():
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            post_data = request.headers
            if 'Authorization' not in post_data:
                return Response({'status':'Failed', 'message': 'Request does not contain authorzation header.'}, status=status.HTTP_403_FORBIDDEN)
            if not 'Bearer' in post_data['Authorization']:
                return Response({'status':'Failed', 'message': 'Request doesn not contain Bearer in Authorization header.'}, status=status.HTTP_403_FORBIDDEN)
            user_token = post_data['Authorization'].split(' ')[1]  
            if not verify_user_from_token(user_token):
                return Response({'status':'Failed', 'message': 'Not valid token. Please sign in again'}, status=status.HTTP_403_FORBIDDEN)
                
            return function(request, *args, **kwargs)
        return wrapper
    return decorator