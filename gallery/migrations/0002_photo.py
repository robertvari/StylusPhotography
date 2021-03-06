# Generated by Django 3.1.1 on 2020-10-24 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Cím')),
                ('image', models.ImageField(upload_to='photos', verbose_name='Kép')),
                ('description', models.TextField(max_length=2000, verbose_name='Leírás')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
            ],
            options={
                'verbose_name_plural': 'Fotók',
            },
        ),
    ]
