# Generated by Django 5.0.6 on 2024-05-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='picture')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=150)),
            ],
        ),
    ]
