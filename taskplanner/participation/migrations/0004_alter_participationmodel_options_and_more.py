# Generated by Django 5.0.3 on 2024-06-11 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_alter_boardmodel_options_remove_boardmodel_progress_and_more'),
        ('participation', '0003_alter_participationmodel_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participationmodel',
            options={'verbose_name': 'Участие в проекте', 'verbose_name_plural': 'Участия в проектах'},
        ),
        migrations.AddConstraint(
            model_name='participationmodel',
            constraint=models.UniqueConstraint(fields=('participant', 'board'), name='Уникальность участия в проекте'),
        ),
    ]
