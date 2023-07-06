# Generated by Django 4.0.10 on 2023-07-06 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 7, 58, 27, 513239, tzinfo=utc)),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
