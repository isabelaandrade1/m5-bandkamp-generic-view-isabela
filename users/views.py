from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
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

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized]

    def get_object(self):
        user_id = self.kwargs['user_id']
        return self.queryset.get(id=user_id)

class UserLogin(TokenObtainPairView):
    serializer_class = JWTSerializer
