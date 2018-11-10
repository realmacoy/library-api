from rest_framework import serializers
from .models import *


class TitleBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleBasic
        fields = [
            'tconst', 'title_type', 'primary_title', 'original_title',
            'is_adult', 'start_year', 'end_year', 'runtime_minutes'
        ]
        read_only_fields = ['tconst']


class TitlePrincipalSerializer(serializers.ModelSerializer):

    class Meta:
        model = TitlePrincipal
        fields = ['id', 'ordering', 'nconst', 'category', 'job', 'characters']
        read_only_fields = ['id']


class TitleSerializer(serializers.ModelSerializer):
    title_principals_tconst = TitlePrincipalSerializer(many=True)

    class Meta:
        model = TitleBasic
        fields = [
            'tconst', 'title_type', 'primary_title', 'original_title',
            'is_adult', 'start_year', 'end_year', 'runtime_minutes',
            'title_principals_tconst'
        ]
        read_only_fields = ['tconst']
