# Generated by Django 4.1.7 on 2023-04-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='code',
            field=models.IntegerField(default=39),
            preserve_default=False,
        ),
    ]
