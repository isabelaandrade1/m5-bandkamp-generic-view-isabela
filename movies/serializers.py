# movies/serializers.py
from rest_framework import serializers
from .models import Movie, MovieOrder

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'rating', 'synopsis', 'added_by']
        read_only_fields = ['id', 'added_by']

    def create(self, validated_data):
        validated_data['added_by'] = self.context['request'].user
        return super().create(validated_data)

class MovieOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieOrder
        fields = ['id', 'movie', 'price', 'ordered_by', 'created_at']  # Corrigido: 'order_date' substituído por 'created_at'
        read_only_fields = ['id', 'ordered_by', 'created_at']

    def create(self, validated_data):
        validated_data['ordered_by'] = self.context['request'].user
        return super().create(validated_data)
