# Generated by Django 4.0.1 on 2022-11-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroomfiles', '0003_classroomfiles_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroomfiles',
            name='results',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='results'),
        ),
    ]