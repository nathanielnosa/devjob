# Generated by Django 3.2.7 on 2021-09-20 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210919_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_photo',
            field=models.ImageField(blank=True, default='img/thumbnail.png', null=True, upload_to=''),
        ),
    ]
