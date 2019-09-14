from django.contrib.auth import authenticate

from users.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from backend_mobile.user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def sign_up(self, request):
        email = request.data['email']
        name = request.data['name']
        password = request.data['password']

        user_is_exist = User.objects.filter(email=email)

        if len(user_is_exist) > 0:
            return Response({'Message': 'Usuário já cadastrado', 'success': False},
                            status=status.HTTP_404_NOT_FOUND)

        new_user = User.objects.create_user(username=email, email=email, name=name)
        new_user.set_password(password)
        new_user.save()
        return Response({'message': 'Cadastro efetuado com sucesso', 'success': True}, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def sign_in(self, request):
        email = request.data['email']
        password = request.data['password']

        if not email or not password:
            return Response({'message': 'Informe os dados para que consiga efetuar o login', 'success': False},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user_is_exist = User.objects.get(email=email)
            if user_is_exist:
                user = authenticate(username=email, password=password)
                token = Token.objects.create(user=user)
                return Response({'message': 'Login efetuado com sucesso', 'success': True, 'token': str(token)},
                                status=status.HTTP_200_OK)
        except Exception as exc:
            print(exc)
            return Response({'message': 'Nenhum usuário encontrado ou os dados foram informados errados',
                             'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)