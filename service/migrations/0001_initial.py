# Generated by Django 5.0.2 on 2024-02-20 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('fees_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area', models.CharField(max_length=255)),
                ('city', models.CharField(choices=[('Kolhapur', 'Kolhapur'), ('Mumbai', 'Mumbai'), ('Surat', 'Surat'), ('Ahmedabad', 'Ahmedabad')], max_length=255)),
                ('state', models.CharField(choices=[('Gujarat', 'Gujarat'), ('Maharashtra', 'Maharashtra')], max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.cat')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subcategory')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.type')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
