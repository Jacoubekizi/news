from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import authenticate
class SingupSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        email = attrs.get('email', )
        username = attrs.get('username', )
        password = attrs.get('password', )
        password2 = attrs.pop('password2', )

        if not email:
            raise serializers.ValidationError('The email is required for singup')
        
        if not username.isalnum:
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        
        if password != password2:
            raise serializers.ValidationError('The password did not matched')
        return attrs
    
    
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=255, min_length=6)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'username', 'tokens']
        extra_kwargs = {
            'password':{'write_only':True,'min_length':6},
            'username':{'read_only':True}
        }

    def get_tokens(self, obj):
        user = CustomUser.objects.get(email = obj['email'])
        token = RefreshToken.for_user(user)
        return {
            'refresh':str(token),
            'access':str(token.access_token)
        }
    
    def validate(self, attrs):
        email = attrs.get('email',)
        password = attrs.get('password',)

        if email is None:
            raise serializers.ValidationError({'message_error':'An email address is required to log in'})
        
        if password is None:
            raise serializers.ValidationError({'message_error':'An password is required to log in'})
        
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError({'message_error':'A user with this email and password was not found.'})

        if not user.is_active:
            raise serializers.ValidationError({'message_error':'This user is not currently activated.'})
        
        return {
            'email':user.email,
            'username':user.username,
            'tokens': self.get_tokens
        }
    
class ListSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token':('Token is expired or invalid'),
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')