# Generated by Django 3.1.6 on 2022-02-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalmatchword',
            name='count',
            field=models.CharField(blank=True, default=1, max_length=100, null=True),
        ),
    ]