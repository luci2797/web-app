# Generated by Django 2.1.2 on 2018-11-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_books_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='year_released',
            field=models.IntegerField(default=2018),
        ),
    ]
