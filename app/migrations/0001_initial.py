# Generated by Django 5.0.7 on 2024-07-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('learning_type', models.CharField(max_length=100)),
                ('algorithm_used', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('dataset_used', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Radnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TitanicSurvivalPredictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.IntegerField()),
                ('pclass', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.FloatField()),
                ('sib_sp', models.IntegerField()),
                ('parch', models.IntegerField()),
                ('ticket', models.CharField(max_length=50)),
                ('fare', models.FloatField()),
                ('cabin', models.CharField(max_length=50)),
                ('embarked', models.CharField(max_length=1)),
            ],
        ),
    ]
