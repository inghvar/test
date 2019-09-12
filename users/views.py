from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from django_filters import rest_framework as filters

from .serializers import UserLoginSerializer, UserSerializer
from users.utils.authentication import token_expire_handler, expires_in
from users.utils.permissions import *
from users.utils.filters import UserFilter
from .models import CustomUser



@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    login_serializer = UserLoginSerializer(data = request.data)
    if not login_serializer.is_valid():
        return Response(login_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    user = authenticate(
            username = login_serializer.data['email'],
            password = login_serializer.data['password'] 
        )
    if not user:
        return Response({'detail': 'Неправильные данные для создания аккаунта'},
                status = status.HTTP_404_NOT_FOUND)
        
    token, _ = Token.objects.get_or_create(user = user)
    
    is_expired, token = token_expire_handler(token)
    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data, 
        'expires_in': expires_in(token),
        'token': token.key
    }, status=status.HTTP_200_OK)


class UserListAPIView(generics.ListAPIView):

    permission_classes = (IsAdmin, )
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = UserSerializer
    

class UserRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
 
    lookup_field = 'pk'
    permission_classes = (IsStaff|IsAdmin )
    serializer_class = UserSerializer
    queryset = CustomUser.objects.filter(is_active=True)


    def get_permissions(self):
        permission_classes = []
        if self.http_method_names == 'retrieve':
            permission_classes = (IsRole_1, )
        elif self.http_method_names == 'update' or self.http_method_names == 'partial_update':
            permission_classes = (IsAdmin, )
        elif self.http_method_names == 'destroy':
            permission_classes = (IsAdmin, )
        return [permission() for permission in permission_classes]


class UserCreateAPIView(generics.CreateAPIView):
 
    permission_classes = (IsRole_2, )
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserFilteredListAPIView(generics.ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
        
