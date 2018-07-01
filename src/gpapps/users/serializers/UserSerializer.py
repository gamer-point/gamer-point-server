from rest_framework.serializers import ModelSerializer

from ..models.User import User

class UserSerializer(ModelSerializer):
    """
    The serializer for User Objects
    """
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        """
        Create and return a new user
        :param validated_data:
        :return: User Object
        """
        
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user
