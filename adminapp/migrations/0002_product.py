# Generated by Django 4.1.7 on 2023-04-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='null.jpg', upload_to='sample')),
            ],
        ),
    ]
