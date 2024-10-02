from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from apps.custom_auth.models import User
from apps.custom_auth.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='login', url_name='login')
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Correo o contraseña son requeridos"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            return Response(
                {"error": "Correo o contraseña incorrectos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        refresh['center'] = {
            "lat": 4.7110,
            "lng": -74.0721
        }
        
        return Response({
            'access': str(refresh.access_token)},
            status=status.HTTP_200_OK
        )
