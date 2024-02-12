"""
    Arquivo de Endpoints da aplicação core
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from core.services import JWTAuthenticationService
class Home(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response({'message': 'Hello World!'}, status=200)


class UsernamePasswordLoginView(APIView):
    permission_classes = []
    def post(self, request):
        email = request.data.get('email').strip()
        password = request.data.get('password')
        
        user = User.objects.filter(email=email).last()

        if not user:
            return Response({'message': 'Conta Inexistente'}, status=401)
        
        if not user.check_password(password):
            return Response({'message': 'Usuário ou senha inválidos'}, status=401)

        access_tokens = JWTAuthenticationService.generate_access_token(user)

        res = {
            'access_token': access_tokens['token'],
            'refresh_token': access_tokens['rtoken']
        }
        return Response(res, status = 200)

