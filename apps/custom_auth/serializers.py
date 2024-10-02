from rest_framework import serializers

from apps.custom_auth.models import User


class MyTokenObtainPairSerializer(serializers.Serializer):
    def get_token(self, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_active'] = user.is_active

        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
