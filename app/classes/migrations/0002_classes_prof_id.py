# Generated by Django 4.0.1 on 2022-10-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='prof_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='prof_id'),
        ),
    ]
