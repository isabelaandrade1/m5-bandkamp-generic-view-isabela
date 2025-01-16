from movies.models import Movie
from .user_factories import create_employee_with_token

def create_movie_with_employee(movie_data=None, employee=None):
    if not employee:
        employee, _ = create_employee_with_token()

    if not movie_data:
        movie_data = {
            "title": "Revolver",
            "duration": "110min",
            "rating": "R",
            "synopsis": "Jake Green is a hotshot gambler...",
        }

    return Movie.objects.create(**movie_data, added_by=employee)

def create_multiple_movies_with_employee(employee, movies_count):
    movies_data = [
        {"title": f"Movie {i}", "duration": "110min", "rating": "R", "added_by": employee}
        for i in range(movies_count)
    ]
    return Movie.objects.bulk_create([Movie(**movie_data) for movie_data in movies_data])
