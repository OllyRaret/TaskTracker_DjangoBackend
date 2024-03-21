# Generated by Django 5.0.3 on 2024-03-21 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('columns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('completed', models.BooleanField()),
                ('on_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='columns.columnmodel')),
            ],
        ),
    ]