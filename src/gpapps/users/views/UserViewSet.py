from rest_framework import filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.authentication import TokenAuthentication

from ..models.User import User
from ..permissions.UpdateOwnUser import UpdateOwnUser
from ..serializers.UserSerializer import UserSerializer


class UserViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                  UpdateModelMixin, GenericViewSet):
    """
    Handles:
    creating an User - Sign Up
    Retrieve a list of users
    Retrieve a specific User
    Update an User
    """
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email', 'username')



