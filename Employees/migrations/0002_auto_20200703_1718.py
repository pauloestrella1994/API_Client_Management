# Generated by Django 2.2.14 on 2020-07-03 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0001_initial'),
        ('Departament', '0001_initial'),
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company.Company'),
        ),
        migrations.AddField(
            model_name='employee',
            name='departament',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Departament.Departament'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
