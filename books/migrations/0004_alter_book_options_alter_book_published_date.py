# Generated by Django 4.0.10 on 2023-07-05 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_published_date_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('Special_status', 'Can read all books')]},
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 14, 28, 11, 51665, tzinfo=utc)),
        ),
    ]