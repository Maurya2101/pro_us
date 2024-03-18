# Generated by Django 5.0.2 on 2024-02-20 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='cat',
            field=models.ForeignKey(choices=[('A/C', 'A/C'), ('Salon', 'Salon'), ('Home Cleaning', 'Home Cleaning')], on_delete=django.db.models.deletion.CASCADE, to='service.cat'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subcategory',
            field=models.ForeignKey(choices=[('A/C repair & service', 'A/C repair & service'), ('Air Cooler Repair', 'Air Cooler Repair'), ('Hair Cut', 'Hair Cut'), ('Massage', 'Massage')], on_delete=django.db.models.deletion.CASCADE, to='service.subcategory'),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.ForeignKey(choices=[('Kolhapur', 'Kolhapur'), ('Mumbai', 'Mumbai'), ('Surat', 'Surat'), ('Ahmedabad', 'Ahmedabad')], on_delete=django.db.models.deletion.CASCADE, to='service.type'),
        ),
    ]