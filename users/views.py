from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import PermissionsPersonalized
from .serializers import UserSerializer, JWTSerializer
from .models import User

class UserView(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized]

    def get(self, request: Request, user_id: int) -> Response:
        user = User.objects.get(id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class UserLogin(TokenObtainPairView):
    serializer_class = JWTSerializer
