# Generated by Django 5.0.7 on 2024-07-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_reservation_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Phone',
            field=models.CharField(max_length=11),
        ),
    ]
