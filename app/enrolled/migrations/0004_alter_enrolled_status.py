# Generated by Django 4.0.1 on 2022-11-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolled', '0003_enrolled_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='status',
            field=models.CharField(blank=True, default='Not Archived', max_length=255, null=True, verbose_name='status'),
        ),
    ]
