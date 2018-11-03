# library-api/library/api/tests/test_models.py

from django.db import IntegrityError
from django.test import TestCase

from ..models import TitleBasic, TitleRating, TitleEpiside


class TestTitleBasicModel(TestCase):
    def setUp(self):
        self.movie = TitleBasic(
            primary_title="Django Unchained", tconst='tt1853728', original_title='Django Unchained', title_type='MOVIE',
            is_adult=False, start_year=2012, end_year=2012, runtime_minutes=165
        )
        self.movie.save()

    def test_movie_creation(self):
        self.assertEqual(TitleBasic.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.movie.primary_title, str(self.movie))

    def test_duplicate_id_not_allowed(self):
        willow = TitleBasic(
            primary_title="Willow", tconst='tt1853728', original_title='Willow', title_type='MOVIE',
            is_adult=False, start_year=1988, end_year=1988, runtime_minutes=126
        )
        willow.save()
        self.assertEqual(TitleBasic.objects.count(), 1)

    def test_title_type_cannot_be_null(self):
        willow = TitleBasic(
            primary_title="Willow", tconst='tt0096446', original_title='Willow', title_type=None,
            is_adult=False, start_year=1988, end_year=1988, runtime_minutes=126
        )
        with self.assertRaises(IntegrityError):
            willow.save()

    def test_allow_blank_fields(self):
        willow = TitleBasic(primary_title="Willow", tconst='tt0096446', title_type='MOVIE')
        willow.save()
        self.assertEqual(TitleBasic.objects.count(), 2)

    def test_successfully_add_new_movie(self):
        willow = TitleBasic(
            primary_title="Willow", tconst='tt0096446', original_title='Willow', title_type='MOVIE',
            is_adult=False, start_year=1988, end_year=1988, runtime_minutes=126
        )
        willow.save()
        self.assertEqual(TitleBasic.objects.count(), 2)

    def test_validate_movie_data(self):
        self.assertEqual(self.movie.start_year, 2012)
        self.assertEqual(self.movie.end_year, 2012)
        self.assertEqual(self.movie.runtime_minutes, 165)


class TestTitleRatingModel(TestCase):
    def setUp(self):
        self.movie = TitleBasic(
            primary_title="Django Unchained", tconst='tt1853728', original_title='Django Unchained', title_type='MOVIE',
            is_adult=False, start_year=2012, end_year=2012, runtime_minutes=165
        )
        self.movie.save()
        self.ratings = TitleRating(tconst=self.movie, average_rating=8.4, num_votes=1159329)
        self.ratings.save()

    def test_ratings_creation(self):
        self.assertEqual(TitleRating.objects.count(), 1)

    def test_ratings_representation(self):
        self.assertEqual("Django Unchained: {}/10".format(self.ratings.average_rating), str(self.ratings))

    def test_must_have_tconst(self):
        rating = TitleRating()
        with self.assertRaises(IntegrityError):
            rating.save()

    def test_no_duplicate_tconst(self):
        rating = TitleRating(tconst=self.movie)
        rating.save()
        self.assertEqual(TitleRating.objects.count(), 1)

    def test_validate_values(self):
        self.assertEqual(self.ratings.average_rating, 8.4)
        self.assertEqual(self.ratings.num_votes, 1159329)

    def test_must_use_object_tconst(self):
        willow = TitleBasic(
            primary_title="Willow", tconst='tt0096446', original_title='Willow', title_type='MOVIE',
            is_adult=False, start_year=1988, end_year=1988, runtime_minutes=126
        )
        willow.save()
        with self.assertRaises(ValueError):
            TitleRating(tconst='tt0096446')


class TestTitleEpisodeModel(TestCase):
    def setUp(self):
        self.show = TitleBasic(
            tconst='tt0805663', primary_title='Jericho', original_title='Jericho', title_type='SERIES',
            is_adult=False, start_year=2006, end_year=2008, runtime_minutes=45
        )
        self.show.save()
        self.show_episode = TitleBasic(
            tconst='tt0494730', primary_title='Pilot', original_title='Pilot', title_type='EPISODE',
            is_adult=False, start_year=2006, runtime_minutes=39
        )
        self.show_episode.save()
        self.episode = TitleEpiside(
            tconst=self.show_episode, parent_tconst=self.show, season_number=1, episode_number=1
        )
        self.episode.save()

    def test_episode_created(self):
        self.assertEqual(TitleEpiside.objects.count(), 1)

    def test_episode_representation(self):
        self.assertEqual("Jericho - S1E1", str(self.episode))

    def test_parent_object(self):
        self.assertEqual(self.episode.parent_tconst, self.show)
