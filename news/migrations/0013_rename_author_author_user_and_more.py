# Generated by Django 4.1.4 on 2022-12-22 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_author',
            new_name='author',
        ),
    ]
