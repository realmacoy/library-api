# Generated by Django 2.1.3 on 2018-11-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_titlecrew'),
    ]

    operations = [
        migrations.AddField(
            model_name='namebasic',
            name='known_for_titles',
            field=models.ManyToManyField(db_column='knownForTitles', to='api.TitleBasic'),
        ),
    ]
