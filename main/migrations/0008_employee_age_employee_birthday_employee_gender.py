# Generated by Django 4.2.1 on 2023-05-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_admin_doctor_alter_employee_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='birthday',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
