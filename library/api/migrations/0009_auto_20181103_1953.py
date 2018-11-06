# Generated by Django 2.1.3 on 2018-11-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181103_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namebasic',
            name='death_year',
            field=models.IntegerField(blank=True, db_column='deathYear', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='namebasic',
            name='primary_professions',
            field=models.CharField(blank=True, db_column='primaryProfessions', default='', max_length=20),
        ),
    ]
