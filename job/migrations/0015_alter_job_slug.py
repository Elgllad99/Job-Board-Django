# Generated by Django 3.2.9 on 2021-12-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
