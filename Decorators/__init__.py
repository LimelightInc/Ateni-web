from functools import wraps
from rest_framework.response import Response
from rest_framework import status

from Authentication import get_all_clients

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