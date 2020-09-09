# Generated by Django 3.1 on 2020-09-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200906_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='scopes', through='articles.TagModel', to='articles.Article'),
        ),
    ]