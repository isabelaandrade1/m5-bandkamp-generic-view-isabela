from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(max_length=127, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(required=False, allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False, allow_null=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        is_employee = validated_data.pop("is_employee", False)

        if is_employee:
            sup_user = User.objects.create_superuser(**validated_data, is_employee=True)
            return sup_user
        return User.objects.create_user(**validated_data, is_employee=False)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(detail="username already taken.")
        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(detail="email already registered.")
        return email


class JWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token
