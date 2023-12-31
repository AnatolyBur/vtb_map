# Generated by Django 3.2.22 on 2023-10-14 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_department_biskvit_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='current_workload',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='WorkloadTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.PositiveIntegerField(default=0)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank.department')),
            ],
            options={
                'verbose_name': 'Нагрузка',
                'verbose_name_plural': 'Нагрузки',
            },
        ),
    ]
