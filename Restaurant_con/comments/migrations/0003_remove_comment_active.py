# Generated by Django 5.0.7 on 2024-07-18 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
