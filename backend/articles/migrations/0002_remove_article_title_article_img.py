# Generated by Django 4.2.1 on 2023-06-22 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]