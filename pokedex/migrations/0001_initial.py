# Generated by Django 4.2 on 2025-01-10 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('F', 'Fuego'), ('P', 'Planta'), ('A', 'Agua'), ('T', 'Tierra'), ('L', 'Lagartija'), ('E', 'Elèctrico')], max_length=30)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=6)),
                ('height', models.DecimalField(decimal_places=4, max_digits=6)),
                ('picture', models.ImageField(upload_to='pokemon_images')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokedex.trainer')),
            ],
        ),
    ]
