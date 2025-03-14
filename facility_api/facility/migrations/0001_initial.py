# Generated by Django 5.1.6 on 2025-02-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_code', models.CharField(max_length=250, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('create_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
