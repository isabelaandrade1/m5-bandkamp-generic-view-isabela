from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from songs.models import Song
from songs.serializers import SongSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import PermissionsPersonalized

class SongView(GenericAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        songs = self.get_queryset()
        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
