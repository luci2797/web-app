# Generated by Django 2.1.2 on 2018-12-11 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181211_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='rating',
            new_name='avg_rating',
        ),
    ]