from rest_framework.test import APITestCase
from rest_framework.views import status
from movies.models import Movie
from tests.factories import create_employee_with_token, create_movie_with_employee, create_multiple_movies_with_employee

class MovieViewsT2Test(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.BASE_URL = "/api/movies/"
        cls.BASE_DETAIL_URL = cls.BASE_URL + "1/"
        cls.maxDiff = None

    def test_movies_listing(self):
        employee, _ = create_employee_with_token()
        movies_count = 5
        create_multiple_movies_with_employee(employee, movies_count)

        response = self.client.get(self.BASE_URL)
        results = response.json().get("results", [])

        expected_count = movies_count
        resulted_count = len(results)
        msg = "Verifique se todos os filmes estão sendo retornados corretamente"
        self.assertEqual(expected_count, resulted_count, msg)

    def test_movie_creation_with_employee_token(self):
        employee, token = create_employee_with_token()
        movie_data = {"title": "Frozen", "duration": "102min"}

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
        response = self.client.post(self.BASE_URL, data=movie_data, format="json")

        expected_status_code = status.HTTP_201_CREATED
        self.assertEqual(expected_status_code, response.status_code)

    def test_movie_creation_without_token(self):
        movie_data = {"title": "Frozen", "duration": "102min"}
        response = self.client.post(self.BASE_URL, data=movie_data, format="json")

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        self.assertEqual(expected_status_code, response.status_code)

    def test_movie_deletion_by_employee(self):
        employee, token = create_employee_with_token()
        movie = create_movie_with_employee(employee=employee)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
        response = self.client.delete(f"{self.BASE_URL}{movie.id}/")

        expected_status_code = status.HTTP_204_NO_CONTENT
        self.assertEqual(expected_status_code, response.status_code)

    def test_movie_deletion_without_token(self):
        movie = create_movie_with_employee()

        response = self.client.delete(f"{self.BASE_URL}{movie.id}/")
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        self.assertEqual(expected_status_code, response.status_code)
