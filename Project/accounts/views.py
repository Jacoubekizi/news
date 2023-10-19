from rest_framework.views import APIView
from .serializers import SingupSerializer, LoginSerializer, ListSerizlizer, LogoutSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class SingupView(generics.GenericAPIView):

    serializer_class  = SingupSerializer
    def post(self, request):

        user_information = request.data
    
        serializer = self.get_serializer(data=user_information)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)
        tokens = {
            'refresh':str(token),
            'accsess':str(token.access_token)
        }
        return Response({'information_students':user_data,'tokens':tokens})
    
class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        return Response(data)
    
class ListView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = ListSerizlizer(users, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)