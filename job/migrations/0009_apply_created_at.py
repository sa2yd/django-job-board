# Generated by Django 5.0 on 2024-01-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
