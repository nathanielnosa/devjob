# Generated by Django 3.2.7 on 2021-12-27 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20211227_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
