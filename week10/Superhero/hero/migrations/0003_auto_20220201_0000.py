# Generated by Django 3.2.9 on 2022-02-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_hero_hero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='hero_image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
