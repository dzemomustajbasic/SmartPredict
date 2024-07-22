# Generated by Django 5.0.7 on 2024-07-13 20:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_titanicsurvivalpredictions_titanicsurvivalprediction'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='titanicsurvivalprediction',
            name='survived',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='titanicsurvivalprediction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]