# Generated by Django 3.2.7 on 2021-12-02 13:04

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211202_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20, null=True, validators=[users.models.validate_name]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20, null=True, validators=[users.models.validate_name]),
        ),
    ]