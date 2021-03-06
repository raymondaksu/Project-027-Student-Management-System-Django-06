# Generated by Django 3.2.2 on 2021-05-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('lecturer_name', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField()),
                ('slides_url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
