# Generated by Django 5.0.2 on 2024-02-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0009_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
