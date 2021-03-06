# Generated by Django 3.0.3 on 2020-06-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutritional_value', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('nutritional_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.NutritionalType')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Product')),
            ],
        ),
    ]
