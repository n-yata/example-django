# Generated by Django 4.1.3 on 2022-11-24 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('contents', models.TextField(blank=True, verbose_name='内容')),
                ('day', models.DateField(default=datetime.date(2022, 11, 25))),
            ],
        ),
    ]