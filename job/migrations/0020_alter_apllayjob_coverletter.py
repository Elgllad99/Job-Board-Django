# Generated by Django 3.2.9 on 2021-12-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_alter_apllayjob_coverletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apllayjob',
            name='coverLetter',
            field=models.TextField(max_length=500),
        ),
    ]
