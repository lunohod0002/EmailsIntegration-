# Generated by Django 5.0.6 on 2024-11-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0006_alter_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='files',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
