# Generated by Django 2.2.7 on 2019-12-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191229_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_as_worker', models.FloatField(default=0.0)),
                ('rate_as_owner', models.FloatField(default=0.0)),
                ('number_votes_worker', models.IntegerField(default=0)),
                ('number_votes_owner', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='registration_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ إنشاء الحساب'),
        ),
    ]
