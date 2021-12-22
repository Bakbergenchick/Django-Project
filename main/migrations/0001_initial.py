# Generated by Django 3.2.8 on 2021-12-18 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('genre', models.CharField(max_length=20, verbose_name='Genre')),
                ('desc', models.TextField(verbose_name='Description')),
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('image', models.ImageField(upload_to='img/', verbose_name='Image')),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': ('Film',),
                'verbose_name_plural': 'Films',
            },
        ),
    ]