# Generated by Django 3.1 on 2020-09-07 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200907_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='topic',
        ),
    ]