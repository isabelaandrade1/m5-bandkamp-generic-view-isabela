from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Movie, MovieOrder
from .serializers import MovieSerializer, MovieOrderSerializer

class MoviePagination(PageNumberPagination):
    page_size = 10

class IsEmployeePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and getattr(request.user, 'is_employee', False)

class MovieView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsEmployeePermission]
    pagination_class = MoviePagination

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsEmployeePermission]

class MovieOrderDetailView(ListCreateAPIView):  # Confirmação do nome correto
    queryset = MovieOrder.objects.all()
    serializer_class = MovieOrderSerializer
    permission_classes = [IsAuthenticated]
