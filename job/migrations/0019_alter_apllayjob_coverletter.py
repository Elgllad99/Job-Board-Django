# Generated by Django 3.2.9 on 2021-12-28 15:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_auto_20211228_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apllayjob',
            name='coverLetter',
            field=ckeditor.fields.RichTextField(),
        ),
    ]