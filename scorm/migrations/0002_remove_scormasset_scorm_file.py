# Generated by Django 5.0.6 on 2024-06-11 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scorm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scormasset',
            name='scorm_file',
        ),
    ]
