# Generated by Django 4.2.1 on 2023-06-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_historie_street'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='title',
            new_name='name',
        ),
    ]
