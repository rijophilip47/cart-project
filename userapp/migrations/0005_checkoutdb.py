# Generated by Django 4.1.7 on 2023-04-24 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(default='', max_length=15)),
                ('country', models.CharField(max_length=15)),
                ('postal_zip', models.CharField(max_length=15)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.cartdb')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]