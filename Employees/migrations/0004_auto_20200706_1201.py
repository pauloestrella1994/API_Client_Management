# Generated by Django 2.2.14 on 2020-07-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
        ('Departament', '0001_initial'),
        ('Employees', '0003_remove_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ManyToManyField(blank=True, null=True, to='Company.Company'),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='departament',
        ),
        migrations.AddField(
            model_name='employee',
            name='departament',
            field=models.ManyToManyField(blank=True, null=True, to='Departament.Departament'),
        ),
    ]
