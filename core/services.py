"""
    Arquivo responsável por guardar as regras de negócio da aplicação core
"""
from rest_framework_simplejwt.tokens import RefreshToken
class JWTAuthenticationService:
    @staticmethod
    def generate_access_token(user):
        """
        Método responsável por gerar um token de acesso para o usuário
        """
        context = {}
        rtoken = RefreshToken.for_user(user)
        rtoken.payload = {**rtoken.payload, **context}
        access_token = str(rtoken.access_token)
        refresh_token = str(rtoken)
        
        return {'token': access_token, 'rtoken': refresh_token}

