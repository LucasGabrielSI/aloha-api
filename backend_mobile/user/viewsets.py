from users.models import User
from django.http import JsonResponse
from rest_framework.decorators import action
from django.contrib.auth import authenticate
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
            return JsonResponse({'Message': 'Usuário já cadastrado', 'success': False, 'status': 400})

        new_user = User.objects.create_user(username=email, email=email, name=name)
        new_user.set_password(password)
        new_user.save()
        return JsonResponse({'message': 'Cadastro efetuado com sucesso', 'success': True, 'status': 201})

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def sign_in(self, request):
        email = request.data['email']
        password = request.data['password']

        if not email or not password:
            return JsonResponse({'message': 'Informe os dados para que consiga efetuar o login', 'success': False,
                                 'status': 400})
        try:
            user_is_exist = User.objects.get(email=email)
            if user_is_exist:
                user = authenticate(username=email, password=password)
                token = Token.objects.get_or_create(user=user)
                return JsonResponse({'message': 'Login efetuado com sucesso', 'success': True, 'token': str(token),
                                     'status': 200})
        except Exception as exc:
            print(exc)
            return JsonResponse({'message': 'Nenhum usuário encontrado ou os dados foram informados errados',
                                 'status': 400, 'success': False})
