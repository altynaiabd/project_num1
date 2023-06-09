# Generated by Django 4.1.7 on 2023-03-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_usermodel_is_active_alter_usermodel_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
