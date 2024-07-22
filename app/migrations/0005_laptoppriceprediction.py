# Generated by Django 5.0.7 on 2024-07-16 16:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_titanicsurvivalprediction_survived_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopPricePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('msi', models.BooleanField(blank=True, null=True)),
                ('amd_cpu', models.BooleanField(blank=True, null=True)),
                ('intel_cpu', models.BooleanField(blank=True, null=True)),
                ('intel_gpu', models.BooleanField(blank=True, null=True)),
                ('amd_gpu', models.BooleanField(blank=True, null=True)),
                ('acer', models.BooleanField(blank=True, null=True)),
                ('weight', models.FloatField()),
                ('flash', models.BooleanField(blank=True, null=True)),
                ('razer', models.BooleanField(blank=True, null=True)),
                ('workstation', models.BooleanField(blank=True, null=True)),
                ('ultrabook', models.BooleanField(blank=True, null=True)),
                ('nvidia_gpu', models.BooleanField(blank=True, null=True)),
                ('gaming', models.BooleanField(blank=True, null=True)),
                ('hdd', models.BooleanField(blank=True, null=True)),
                ('cpu_frequency', models.FloatField()),
                ('ssd', models.BooleanField(blank=True, null=True)),
                ('notebook', models.BooleanField(blank=True, null=True)),
                ('screen_height', models.IntegerField()),
                ('screen_width', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]