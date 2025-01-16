from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from albums.models import Album
from albums.serializers import AlbumSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import PermissionsPersonalized

class AlbumView(GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(added_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        albums = self.get_queryset()
        serializer = self.get_serializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
