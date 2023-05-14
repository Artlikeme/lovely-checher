# Generated by Django 4.1.7 on 2023-05-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_descriptionforitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='average_check',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='date_foundation',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='item',
            name='hours',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='item',
            name='parking',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.DeleteModel(
            name='DescriptionForItem',
        ),
    ]
