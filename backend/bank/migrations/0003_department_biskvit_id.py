# Generated by Django 3.2.22 on 2023-10-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20231014_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='biskvit_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
