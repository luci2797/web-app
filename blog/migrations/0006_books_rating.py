# Generated by Django 2.1.2 on 2018-11-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_books_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
