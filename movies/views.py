# movies/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Movie, MovieOrder
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework.pagination import PageNumberPagination

class MoviePagination(PageNumberPagination):
    page_size = 10

class MovieView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MoviePagination

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class MovieOrderDetailView(ListCreateAPIView):
    queryset = MovieOrder.objects.all()
    serializer_class = MovieOrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(ordered_by=self.request.user)

