# Generated by Django 4.2 on 2023-05-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_actorid_creativeteam_play_remove_actor_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actorid',
            name='photo',
            field=models.CharField(max_length=255, null=True, verbose_name='Фото'),
        ),
    ]
