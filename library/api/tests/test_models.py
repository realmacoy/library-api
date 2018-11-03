# library-api/library/api/tests/test_models.py

from django.db import IntegrityError
from django.test import TestCase

from ..models import Movie


class TestMovieModel(TestCase):
    def setUp(self):
        self.movie = Movie(
            primary_title="Django Unchained", tconst='tt1853728', original_title='Django Unchained', title_type='MOVIE',
            is_adult=False, start_year=2012, end_year=2012, runtime_minutes=165
        )
        self.movie.save()

    def test_movie_creation(self):
        self.assertEqual(Movie.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.movie.primary_title, str(self.movie))

    def test_duplicate_id_not_allowed(self):
        with self.assertRaises(IntegrityError):
            Movie.objects.create(
                primary_title="Willow", tconst='tt1853728', original_title='Willow', title_type='MOVIE',
                is_adult=False, start_year=1988, end_year=1988, runtime_minutes=126
            )

    def test_title_type_cannot_be_null(self):
        willow = Movie(
            primary_title="Willow", tconst='tt0096446', original_title='Willow', title_type=None,
            is_adult=False, start_year=1988, end_year=1988, runtime_minutes=126
        )
        with self.assertRaises(IntegrityError):
            willow.save()
