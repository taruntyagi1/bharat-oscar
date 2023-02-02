# Generated by Django 3.2.16 on 2023-01-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_about_education_header_logo_header_menu_interviews_what_we_do'),
    ]

    operations = [
        migrations.AddField(
            model_name='header_logo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='header_menu',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='press_image',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='press_release',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
