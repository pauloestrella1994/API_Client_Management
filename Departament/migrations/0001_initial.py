# Generated by Django 2.2.14 on 2020-07-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departament_name', models.CharField(help_text="departament's name", max_length=100)),
            ],
        ),
    ]
