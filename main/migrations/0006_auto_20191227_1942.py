# Generated by Django 2.2.8 on 2019-12-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191227_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='./media', verbose_name='صورة شخصية'),
        ),
    ]
