# Generated by Django 5.0.7 on 2024-07-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_reservation_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
            ],
        ),
    ]
