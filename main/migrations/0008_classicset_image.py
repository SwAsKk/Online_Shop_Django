# Generated by Django 4.0.1 on 2022-05-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_bakedsets_deserts_drinks_hotandsalads_magrolls_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classicset',
            name='image',
            field=models.ImageField(null=True, upload_to='\\images'),
        ),
    ]
