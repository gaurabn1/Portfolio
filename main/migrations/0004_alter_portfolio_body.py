# Generated by Django 5.0.8 on 2024-08-07 09:11

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_skill_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
