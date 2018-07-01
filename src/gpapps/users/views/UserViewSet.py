from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from ..models.User import User
from ..permissions.UpdateOwnUser import UpdateOwnUser
from ..serializers.UserSerializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Handles create and update Users
    """
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email', 'username')
