# Generated by Django 5.0.3 on 2024-03-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0002_alter_url_long_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='alias',
            field=models.CharField(max_length=12),
        ),
    ]