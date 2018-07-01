from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

from ..serializers.JSONWebTokenSerializer import JSONWebTokenSerializer

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class ObtainJSONWebToken(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.object.get('user')
            
            if user.is_tfa_enabled == True:
                response_data = {
                    'token': None,
                    "require": 'two_factor_authentication'
                }
            elif not user.is_email_verified:
                response_data = {
                    'token': None,
                    "require": 'verify_email'
                }
            else:
                token = serializer.object.get('token')
                response_data = jwt_response_payload_handler(token, user, request)
            
            response = Response(response_data)
            
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

obtain_jwt_token = ObtainJSONWebToken.as_view()
