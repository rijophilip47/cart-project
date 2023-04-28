# Generated by Django 4.1.7 on 2023-04-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_checkoutdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
    ]
