# Generated by Django 4.1.1 on 2023-01-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_userrole_new_applicationuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationuser',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
