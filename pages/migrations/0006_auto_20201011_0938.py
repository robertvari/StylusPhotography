# Generated by Django 3.1.1 on 2020-10-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201011_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='siteinfo',
            old_name='logo',
            new_name='image',
        ),
    ]