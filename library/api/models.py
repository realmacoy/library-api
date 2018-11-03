from django.db import models


class TitleBasics(models.Model):
    TITLE_TYPES = (
        ('MOVIE', 'Movie'),
        ('SHORT', 'Short'),
        ('SERIES', 'TV Series'),
        ('EPISODE', 'TV Episode'),
        ('VID', 'Video')
    )

    tconst = models.CharField(max_length=10, primary_key=True, null=False, blank=False, unique=True)
    title_type = models.CharField(max_length=15, null=False, blank=False, choices=TITLE_TYPES, db_column='titleType')
    primary_title = models.CharField(max_length=255, null=False, blank=False, db_column='primaryTitle')
    original_title = models.CharField(max_length=255, null=True, blank=True, db_column='originalTitle')
    is_adult = models.BooleanField(default=False, db_column='isAdult')
    start_year = models.IntegerField(null=True, blank=True, default=None, db_column='startYear')
    end_year = models.IntegerField(null=True, blank=True, default=None, db_column='endYear')
    runtime_minutes = models.IntegerField(null=False, default=0, db_column='runtimeMinutes')
    # TODO: add genres here (foreign key) or many-to-many

    def __str__(self):
        return self.primary_title

