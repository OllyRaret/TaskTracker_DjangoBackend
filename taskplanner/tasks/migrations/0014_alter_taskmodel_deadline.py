# Generated by Django 5.0.3 on 2024-06-11 22:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_alter_taskmodel_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='deadline',
            field=models.DateField(blank=True, help_text='Формат даты YYYY-MM-DD', null=True, validators=[django.core.validators.MinValueValidator(datetime.date(2024, 6, 12), message='Дедлайн не может быть раньше сегодняшнего числа')], verbose_name='Дедлайн'),
        ),
    ]
