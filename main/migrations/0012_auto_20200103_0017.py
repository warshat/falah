# Generated by Django 2.2.8 on 2020-01-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200103_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='number_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
    ]