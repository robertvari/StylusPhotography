# Generated by Django 3.1.1 on 2020-10-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_siteinfo_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Címsor')),
                ('content', models.TextField(max_length=5000, verbose_name='Üzenet')),
            ],
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo', verbose_name='Logo'),
        ),
    ]
