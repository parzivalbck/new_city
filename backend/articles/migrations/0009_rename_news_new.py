# Generated by Django 4.2.1 on 2023-06-24 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_news_alter_article_key'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
    ]
