from django.db import models


class TitleBasic(models.Model):
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


class TitleRating(models.Model):
    tconst = models.OneToOneField(
        TitleBasic, on_delete=models.CASCADE, primary_key=True,
        null=False, blank=False, related_name='title_rating_tconst'
    )
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, db_column='averageRating')
    num_votes = models.PositiveIntegerField(default=0, db_column='numVotes')

    def __str__(self):
        return "{}: {}/10".format(self.tconst, self.average_rating)


class TitleEpiside(models.Model):
    tconst = models.OneToOneField(
        TitleBasic, on_delete=models.CASCADE, primary_key=True,
        null=False, blank=False, related_name='title_episode_tconst'
    )
    parent_tconst = models.OneToOneField(
        TitleBasic, on_delete=models.CASCADE, null=False, blank=False,
        db_column='parentTconst', related_name='title_episode_parent_tconst'
    )
    season_number = models.SmallIntegerField(db_column='seasonNumber', default=0)
    episode_number = models.SmallIntegerField(db_column='episodeNumber', default=0)

    def __str__(self):
        return "{} - S{}E{}".format(self.parent_tconst, self.season_number, self.episode_number)


class Profession(models.Model):
    role = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __str__(self):
        return self.role


class NameBasic(models.Model):
    nconst = models.CharField(max_length=10, primary_key=True, null=False, blank=False, unique=True)
    primary_name = models.CharField(max_length=100, blank=False, null=False, db_column='primaryName')
    birth_year = models.IntegerField(null=True, default=None, db_column='birthYear')
    death_year = models.IntegerField(null=True, default=None, blank=True, db_column='deathYear')
    primary_professions = models.ManyToManyField(Profession)
    known_for_titles = models.ManyToManyField(TitleBasic, db_column='knownForTitles', blank=True)

    def __str__(self):
        death = ''
        if self.death_year is not None:
            death = self.death_year
        return self.primary_name + " ({}-{})".format(self.birth_year, death)


class TitleCrew(models.Model):
    tconst = models.OneToOneField(
        TitleBasic, on_delete=models.CASCADE, primary_key=True,
        null=False, blank=False, related_name='title_crew_tconst'
    )
    directors = models.ManyToManyField(NameBasic, related_name='directors+')
    writers = models.ManyToManyField(NameBasic, related_name='writers+')

    def __str__(self):
        return str(self.tconst)


class TitlePrincipal(models.Model):
    id = models.AutoField(primary_key=True)
    tconst = models.OneToOneField(
        TitleBasic, on_delete=models.CASCADE,
        null=False, blank=False, related_name='title_principals_tconst'
    )
    ordering = models.IntegerField(default=0, null=False, blank=True)
    nconst = models.OneToOneField(
        NameBasic, on_delete=models.SET_NULL, null=True, blank=False,
        related_name='title_principals_nconst'
    )
    category = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    job = models.CharField(max_length=50, default=None, null=True, blank=True)
    characters = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.tconst) + " - " + str(self.nconst)